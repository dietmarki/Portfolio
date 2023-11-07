# select = auswählen, distinct = einmalig, from = von wo (z.b.Tabelle), as '' = umbenennen;
# mehrere queries auf einem sheet bzw. einer sql-datei trennt man durch " ; " !!!

select distinct

first_name as 'Vorname'

from employees
;
# alle spalten einer tabelle = "*", genaue anzahl der ausgabe von zeilen = "limit"

select

*

from salaries

limit 10
;
# where = eine art if-bedingung (hier: alle Gehälter über 60000)

select

*

from salaries

where salary > 40000 and salary < 41000
;
# ungleich-operator: "!=" oder "<>"

select

first_name as "Vorname",
last_name as "Nachname",
gender as "Geschlecht"

from employees

where first_name = "Berni" and gender != "F"
;
# bei datum, welches bis weit in die zukunft gelten soll
# gibt das programm die jahreszahl "9999" an!!!

# "and" ist immer mächtiger als "or"
#  --->  ...or...and... gilt folgendermaßen:
#        ...or...(...and...)  - bedingungen verbunden mit "and" werden dann als gesamter block verwendet!!!

select
*
from titles
where title = "Senior Engineer"
or from_date >= "1986-01-01"
and to_date <= "2000-01-01"
;
# Beispiel
select
*
from titles
where not title = "Staff" and from_date >= "1989-01-01"
;
# wildcard ist eine art joker und wird mit "like "_%_" umgesetzt!
# bei buchstaben (erster/letzter) und bei zahlen direkt an den zahlen (beim datum nicht am "-", sonst nur dieser inhalt, wie monat bei datum!!)
# bei exakt einem buchstaben an einer bestimmten stelle mit unterstrich: "..._" (auch mehrere unterstriche möglich)

select
*
from employees
where
first_name like "die%" and birth_date like "1965%" and last_name like "%n%" and hire_date like "%05-__"
or last_name like "Kranzdor_"
;
# sortieren mit dem befehl "order by" ("asc" voreingestellt mit aufsteigend, mit "desc" absteigend)
# where-bedingun immer vor dem sortierbefehl

select salary from salaries

where salary < 39000

order by salary desc
;
# min- und max-funktion zwischen select und from (mehrere sortierfunktionen nebeneinander möglich!):
select
max(salary) as "größtes Gehalt",
min(salary) as "kleinstes Gehalt"
from salaries
;
# berechnungsfunktionen count()
# mit in der Klammer die definition der genauen auswahl:
select
count(distinct emp_no) as "Anzahl der Gehaltserhöhungen der Mitarbeiter"
from salaries
;
# berechnungsfunktionen sum():
select sum(salary)as "Summe der Gehälter" from salaries
where from_date like "1991%" or to_date like "1991%"
;
# mehrere berechnungsfunktionen sum(), summe und avg(), durchschnitt:
select
sum(salary)as "Summe der Gehälter",
avg(salary) as "Durchschnitt der Gehälter",
count(distinct emp_no) as "Anzahl der Gehälter der Mitarbeiter"
from salaries
where from_date like "1990%"
;
# mit gruppieren "group by" kann man berechnungen auch für bestimmte bereiche (z.b. personen) umsetzen:
select
sum(salary) as "Summe der Gehälter",
emp_no as "Personalnummer"
from salaries
where emp_no < "10050"
group by emp_no
;
# mit mehreren gruppierungen:
select
first_name,
gender as "Geschlecht",
count(first_name) as "Vornamen"
from employees
group by first_name, gender
order by first_name
;
# where-statement mit mehreren elementen über "in(...,...,..)"
# oder "not in ()":

select * from departments
where dept_name in ("Finance","Marketing","Production")
;

# eine select-statement in einem statement
# über select innerhalb des where-statments "where .. in (select...)":

select * from titles
where title in (
select title from titles where title = "Senior Engineer" and emp_no = "10004")
;

# einen bestimmten datumsbereich herausholen
# für heutiges datum befehl "curdate()":

select * from employees
where hire_date between "1985-11-10" and "1985-11-22"
;

# z.b. alle employees, die manager sind ---> also verschiedene tabellen verbinden:
# schnittmengen der tabellen kürzel "xx" der haupttabelle und "innerjoin" und "on"
# mit dem jeweiligen kürzel für die spalten "xx.spalte" = "xx.spalte"
# möglich mit beliebig vielen tabellen!!!

select
e.first_name,
e.last_name,
e.gender,
dm.dept_no,
d.dept_name
from employees e
inner join dept_manager dm on e.emp_no = dm.emp_no
inner join departments d on dm.dept_no = d.dept_no
where dm.to_date > curdate()
;

# "where"-statement funktioniert nie bei aggregats-funktionen (sum,count,..)!!!
# deswegen benutzt man stattdessen "having":

                      # wichtig: statements genau in dieser reihenfolge!!!

select
e.first_name as "Vorname",
e.last_name as "Nachname",
count(*) as "Anzahl Gehaltserhöhungen"
from salaries s
inner join employees e on e.emp_no = s.emp_no
where from_date >= "1990-01-01"
group by e.first_name, e.last_name
having count(*) >= 5
order by count(*)
;


# wenn man vorab mit bedingungen bei mehreren JOINs filtern will,
# dann die bedingung direkt im anschluss einfügen:
#           "inner join...as...on...filterbedingungen"
# vorteil: es wird sofort gefiltert >< "having" oder "where"
select
*
from employees e1
inner join employees e2 on e2.emp_no != e1.emp_no and e1.gender = e2.gender and year(e1.birth_date) < 1960