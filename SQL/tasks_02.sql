# 1.Lass dir eine Tabelle ausgeben, die den Vor- und Nachnamen der
# Schauspielende, die Anzahl an Filmen, in denen sie mitgespielt
# haben und die durchschnittliche Länge des Filmes widerspiegelt.

select
a.first_name as "Vorname",
a.last_name as "Nachname",
count(distinct f.film_id) as "Anzahl der Filme",
avg(f.length) as "durchscnittliche Länge"
from film_actor f_a
inner join actor a on a.actor_id = f_a.actor_id
inner join film f on f.film_id = f_a.film_id
group by a.actor_id
;

# 2.Du möchtest die Genres category und den Umsatz
# rental_rate bewerten. Lass dir dazu eine Tabelle ausgeben,
# die das Genre, die Anzahl an Titel, den durchschnittlichen
# Umsatz pro Titel und den max. Umsatz pro Titel ausgibt.
select
distinct c.name,
count(f_c.category_id) as "Anzahl",
avg(f.rental_rate)as "Avg",
max(f.rental_rate) as "Max"
from film_category f_c
inner join category c on c.category_id = f_c.category_id
inner join film f on f.film_id = f_c.film_id
group by c.name,f_c.category_id
;

# 3.Welche drei Genres haben den günstigsten Mietpreis?
select
distinct c.name,
min(f.rental_rate) as "Min"
from film_category f_c
inner join category c on c.category_id = f_c.category_id
inner join film f on f.film_id = f_c.film_id
group by c.name
;

# 4.Optional: Finde alle Filme, die zur Kategorie Sci-Fi gehören und
# lass die restlichen Kategorien ohne Werte. Hier soll wieder kein
# WHERE benutzt werden, sondern ein LEFT JOIN. Mehr zum
# Thema kommt erst nächste Woche.

select
f.film_id,
f.title,
c.name
from film f
inner join film_category f_c on f_c.film_id = f.film_id
right join category c on f_c.category_id = c.category_id and c.name = "Sci-Fi"
