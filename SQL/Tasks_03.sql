# 1. Selektiere alle Mitarbeitende und die passende Führungskraft.
select
mit.emp_no as "Mitarbeiter_ID",
mit.first_name as "Mitarbeiter_Vorname",
mit.last_name as "Mitarbeiter_Nachname",
dm.emp_no as "Manager_ID",
man.first_name as "Vorname_Manager",
man.last_name as "Nachname_Manager",
d.dept_no as "Department_no",
d.dept_name as "Department_Name"
from employees mit
inner join dept_emp de on de.emp_no = mit.emp_no
inner join departments d on d.dept_no = de.dept_no
inner join dept_manager dm on dm.dept_no = d.dept_no
inner join employees man on man.emp_no = dm.emp_no
where de.to_date > curdate() and dm.to_date > curdate()
order by dm.dept_no
;

# 2. Erweitere die Abfrage aus Aufgabe 1 um eine neue Spalte, die anzeigt, ob jemand
# eine Führungskraft oder Arbeitskraft ist. Führungskraft soll erscheinen, wenn der
# Mitarbeiter auch zugleich ein Department Manager ist!
select
mit.emp_no,
mit.first_name as "Mitarbeiter_Vorname",
mit.last_name as "Mitarbeiter_Nachname",
dm.emp_no as "Manager_ID",
man.first_name as "Vorname_Manager",
man.last_name as "Nachname_Manager",
d.dept_no as "Department_no",
d.dept_name as "Department_Name",
case
	when dm.emp_no = de.emp_no
    then "Führungskraft"
    else "Mitarbeiter"
end "Beschäftigung"
from employees mit
inner join dept_emp de on de.emp_no = mit.emp_no
inner join departments d on d.dept_no = de.dept_no
inner join dept_manager dm on dm.dept_no = d.dept_no
inner join employees man on man.emp_no = dm.emp_no
where de.to_date > curdate() and dm.to_date > curdate()
order by Beschäftigung
;

# 3.Erweitere die Abfrage aus Aufgabe 2 um eine neue Spalte, die anzeigt, ob das
# aktuelle Gehalt nach einem Aufschlag von 10% immer noch unter 100.000 liegt.
# Beispiel:
#      ● Derzeitiges Gehalt 95.000: NEIN, da 95.000 + 10% Aufschlag > 100.000
#      ● Derzeitiges Gehalt 80.000: JA, da 80.000 + 10% Aufschlag < 100.000
select
mit.emp_no,
mit.first_name as "Mitarbeiter_Vorname",
mit.last_name as "Mitarbeiter_Nachname",
dm.emp_no as "Manager_ID",
man.first_name as "Vorname_Manager",
man.last_name as "Nachname_Manager",
d.dept_no as "Department_no",
d.dept_name as "Department_Name",
s.salary as "MA_Gehalt",
s.salary * 1.1 as "Gehaltserhöhung",
case
	when dm.emp_no = de.emp_no
    then "Führungskraft"
    else "Mitarbeiter"
end "Beschäftigung",
case
	when (s.salary * 1.1) > 100000
    then "NEIN"
    else "JA"
end "Gehaltsniveau"
from employees mit
inner join dept_emp de on de.emp_no = mit.emp_no
inner join departments d on d.dept_no = de.dept_no
inner join dept_manager dm on dm.dept_no = d.dept_no
inner join employees man on man.emp_no = dm.emp_no
inner join salaries s on mit.emp_no = s.emp_no
where de.to_date > curdate() and dm.to_date > curdate() and s.to_date > curdate()
order by Gehaltsniveau
;

# 4.Erweitere die Abfrage aus Aufgabe 3 um eine neue Spalte, die anzeigt, ob das
# aktuelle Gehalt höher oder niedriger als der Mittelwert der aktuellen Salaries ist.
select
mit.emp_no as "Mitarbeiter_ID",
mit.first_name as "Mitarbeiter_Vorname",
mit.last_name as "Mitarbeiter_Nachname",
dm.emp_no as "Manager_ID",
man.first_name as "Vorname_Manager",
man.last_name as "Nachname_Manager",
d.dept_no as "Department_no",
d.dept_name as "Department_Name",
s.salary as "MA_Gehalt",
#s.salary * 1.1 as "mit Gehaltserhöhung",
#(select sum(salary) / count(emp_no) from salaries) as "AVG_Gehalt",
case
	when dm.emp_no = de.emp_no
    then "Führungskraft"
    else "Mitarbeiter"
end "Beschäftigung",
case
	when (s.salary * 1.1) > 100000
    then "NEIN"
    else "JA"
end "Gehaltsniveau",
case
	when s.salary > (select sum(salary) / count(emp_no) from salaries)
    then "Mehr"
    else "Weniger"
end "M/W_AVG_Salary"
from employees mit
inner join dept_emp de on de.emp_no = mit.emp_no
inner join departments d on d.dept_no = de.dept_no
inner join dept_manager dm on dm.dept_no = d.dept_no
inner join employees man on man.emp_no = dm.emp_no
inner join salaries s on mit.emp_no = s.emp_no
where de.to_date > curdate() and dm.to_date > curdate() and s.to_date > curdate()
group by s.salary, mit.emp_no, dm.emp_no, d.dept_no
#order by Gehaltsniveau
;

# 5. Lass dir eine Übersicht über alle aktuellen Manager ausgeben, deren
# Abteilungsnamen und die Anzahl an Mitarbeitern, die in deren Abteilungen
# arbeiten.
select
dm.emp_no as "Manager_ID",
e.first_name as "Manager_Vorname",
e.last_name as "Manager_Nachname",
d.dept_name as "Abteilung",
count(de.emp_no) as "Anzahl_MA"
from dept_manager dm
inner join employees e on dm.emp_no = e.emp_no
inner join departments d on d.dept_no = dm.dept_no
inner join dept_emp de on d.dept_no = de.dept_no
where dm.to_date > curdate() and de.to_date > curdate()
group by d.dept_name, dm.emp_no
;

# 6. Erweitere die Abfrage aus Aufgabe 5, indem nur die Abteilungen angezeigt werden,
# die mehr Mitarbeitende als das Sales Department haben.
select
dm.emp_no as "Manager_ID",
e.first_name as "Manager_Vorname",
e.last_name as "Manager_Nachname",
d.dept_name as "Abteilung",
count(de.emp_no) as "Anzahl_MA"
from dept_manager dm
inner join employees e on dm.emp_no = e.emp_no
inner join departments d on d.dept_no = dm.dept_no
inner join dept_emp de on d.dept_no = de.dept_no
where dm.to_date > curdate() and de.to_date > curdate()
group by d.dept_name, dm.emp_no
having count(de.emp_no) >= (select count(emp_no) from dept_emp where dept_no = "d007" and to_date > curdate())
#order by count(de.emp_no)
;
