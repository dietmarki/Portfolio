# 1. Was ist das durchschnittliche Gehalt für jedes Geschlecht in den
# unterschiedlichen Abteilungen?
select
e.gender as "Geschlecht",
d.dept_name as "Abteilung",
avg(s.salary) as "durchschnittliches Gehalt"
from salaries s
inner join employees e on e.emp_no = s.emp_no
inner join dept_emp d_e on d_e.emp_no = s.emp_no
inner join departments d on d.dept_no = d_e.dept_no
where d_e.to_date > curdate() and s.to_date > curdate()
group by e.gender,d.dept_name
;

# 2.Welche Abteilung verdient am besten?
# Antwort: Abteilung "Sales"
select
e.gender as "Geschlecht",
d.dept_name as "Abteilung",
avg(s.salary) as "durchschnittliches Gehalt"
from salaries s
inner join employees e on e.emp_no = s.emp_no
inner join dept_emp d_e on d_e.emp_no = s.emp_no
inner join departments d on d.dept_no = d_e.dept_no
where d_e.to_date > curdate() and s.to_date > curdate()
group by e.gender,d.dept_name
order by avg(s.salary) desc
;

# 3.Wie viele Mitarbeiter arbeiten in den Abteilungen?
select
e.gender as "Geschlecht",
d.dept_name as "Abteilung",
avg(s.salary) as "durchschnittliches Gehalt",
count(distinct e.emp_no) as "Anzahl MAs"
from salaries s
inner join employees e on e.emp_no = s.emp_no
inner join dept_emp d_e on d_e.emp_no = s.emp_no
inner join departments d on d.dept_no = d_e.dept_no
where d_e.to_date > curdate() and s.to_date > curdate()
group by e.gender,d.dept_name
order by avg(s.salary) desc
;

# 4.Welche und wie viele Abteilungs-Geschlecht-Kombinationen aus
# Aufgabe 3 haben mehr als 10.000 Mitarbeiter.
select
e.gender as "Geschlecht",
d.dept_name as "Abteilung",
avg(s.salary) as "durchschnittliches Gehalt",
count(distinct e.emp_no) as "Anzahl MAs"
from salaries s
inner join employees e on e.emp_no = s.emp_no
inner join dept_emp d_e on d_e.emp_no = s.emp_no
inner join departments d on d.dept_no = d_e.dept_no
where d_e.to_date > curdate() and s.to_date > curdate()
group by e.gender,d.dept_name
having count(distinct e.emp_no) > 10000
order by avg(s.salary) desc
;

# 5.Erstelle eine Tabelle mit allen Paaren von Mitarbeitern des
# gleichen Geschlechts, die vor 1960 geboren sind. Benutze dabei
# keine WHERE-Bedingung und beachte die reflexive Relation, d.h.
# alle Reihen, wo ein Mitarbeiter mit sich selbst paart.
select
*
from employees e1
inner join employees e2 on e2.emp_no != e1.emp_no and e1.gender = e2.gender and year(e1.birth_date) < 1960
