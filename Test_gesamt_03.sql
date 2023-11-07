# QUERIES: LEFT JOIN: employees und dept_managers
# --> menge: employees(links/haupttabelle) und die schnittmenge der beiden
#            (dept_managers(rechts) ohne schnittmenge werden nicht ausgegeben!! --> null-werte)
#            --> "alle mitarbeiter inkl. name/geb./geschl und ob jemand manager ist und welche gehälter er hat (jetzige/vergangene)"
select *
from employees e
inner join dept_manager d_m on d_m.emp_no = e.emp_no
left join salaries s on s.emp_no = e.emp_no
where d_m.emp_no is not null and s.to_date > curdate()       # keine null-werte und nur aktuell angestellte
;

# QUERIES: RIGHT JOIN: employees und dept_managers
# --> menge: dept_managers(rechts/nebentabelle) und die schnittmenge der beiden
#            (employees(links/haupttabelle) ohne schnittmenge werden nicht ausgegeben!!--> null-werte)
#            --> "alle mitarbeiter, die dept-manager sind"
select *
from employees e
right join dept_manager d_m on d_m.emp_no = e.emp_no      # wichtig:
right join salaries s on s.emp_no = e.emp_no              #    die reihenfolge der joins und auf welche man mit "on" zugreift!!!
where d_m.to_date > curdate()
;

# QUERIES: LEFT OUTER JOIN: employees und dept_managers
# --> menge: employees(links/haupttabelle) ohne die schnittmenge der beiden
#           --> OUTER wird über die null-bedingung mit where umgesetzt
#               (gegenprobe möglich über "and einzelne person außerhalb dieser menge (z.b.ein manager)"
#     alle mitarbeiter ohne die manager
select *
from employees e
left join dept_manager d_m on d_m.emp_no = e.emp_no
where d_m.emp_no is null #and e.emp_no = "110085"  (als mögliche gegenprobe --> kein wert!)
;

# QUERIES: FULL OUTER JOIN: employees und dept_managers --> nur indirekter weg bei mysql möglich!!
#  --> menge: mit UNION (grundvoraussetzung: anzahl der columns muß übereinstimmen)
#             --> alle elemente werden kombiniert und anschließend die duplikate entfernt!!
#                 LEFT JOIN - UNION - RIGHT JOIN
#  --> alle mitarbeiter und alle manager (--> ohne duplikate, z.b. "kunden und lieferanten gesamt")
select *
from employees e
left join dept_manager d_m on d_m.emp_no = e.emp_no
union         # entfernt zusätzlich die duplikate
select *
from employees e
right join dept_manager d_m on d_m.emp_no = e.emp_no
;

# Query - NULL
# schreibweise: --> ifnull(spalte, "...") as "..."
select
e.emp_no as "Personalnummer",
ifnull(d_m.dept_no, "Kein Manager") as "Department"
from employees e
left join dept_manager d_m on d_m.emp_no = e.emp_no
;

# QUERY - Operatoren
# +,-,*,/,%
# z.b. mit "% 2" gerade/ ungerade monate selektieren
select
salary as "Gehalt",
salary * 1.2 as "Gehaltserhöhung"
from salaries
;

# QUERY - mit Bedingungen und Operatoren
# alle gehälter der mitarbeiter des unternehmens in unterteilungen
# spitze: > 100000, mitte: 50000 - 100000, gering
# bedingungen für ausgaben: --> "case   when...then ...when...then... else...then... end as ... "
select
emp_no as "Personalnummer",
salary as "Gehalt",
case
when salary > 100000
	then "SPITZE"
when salary between 50000 and 100000
	then "Mitte"
else "gering"
end as "Gehaltsklasse"
from salaries
where to_date > curdate()               # aktuell!!
;

# Query - SUBQUERY im from-block
# voraussetzung: haupttabelle hat aggregatsfunktion (anzahl der geschlechter)
#               -->  der Output muss genau eine Zeile und eine Spalte besitzen!
# die haupttabelle wird in ()-klammern eingefaßt, neu benannt ("tabelle_1") und eine subquery erstellt
# hierbei bezieht man sich auf die in der haupttabelle definierten Namen ("Anzahl")
select
avg(Anzahl)
from
	(select
	gender as "Geschlecht",
	count(*) as "Anzahl"
	from employees
	group by gender) as tabelle_1
;

# SUBQUERY im join-block:
SELECT *
FROM salaries s
INNER JOIN (SELECT
			de.dept_no,
            avg(s.salary) AS "salary_pro_dep"
			FROM employees e
			inner join dept_emp de on e.emp_no = de.emp_no
			inner join salaries s on e.emp_no = s.emp_no
			WHERE e.last_name LIKE 'M%'
			) as sq1
			ON s.emp_no = sq1.emp_no
where to_date > curdate()

;

# SUBQUERY in einer where-bedingung
# --> gut einzelinformationen!!! (bei mehr informationen notwendig --> joins verwenden!!)
select
*
from employees
where emp_no in 
	(select
    emp_no
    from salaries
    where salary > 100000 and to_date > curdate())
;

# mehrere SUBQUERIES verschachtelt im select-block:
SELECT
*,
(SELECT count(DISTINCT emp_no) FROM employees) AS "Anzahl_MA",
(SELECT avg(salary) FROM salaries) AS "MW_Salary",
salary / (SELECT avg(salary) FROM salaries) * 100 AS "Salary%"
FROM salaries
#GROUP BY salary
;

# INDEX/ INDIZES macht die queries schneller!!!
# für spalten, die man sehr häufig verwendet in einer sehr großen datenbank!!
# speed der abfrage besser, es braucht aber auch mehr speicherplatz

select * from employees where first_name = "Mary"                           # abfrage 0.3 sec!!!
;

create index vorname_index
on employees (first_name)
;
select * from employees
where first_name = "Mary"                                                # abfrage 0.000 sec!!!
;
