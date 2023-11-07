# aufgabe 03: --> anfragen beantworten

# 1. Was ist der minimale, maximale und der durchschnittliche Preis für eine Buchung?
SELECT 
    MIN(preis) AS 'minimaler Preis',
    MAX(preis) AS 'maximaler Preis',
    AVG(preis) AS 'durchschnittlicher Preis'
FROM
    buchung
;

# 2. Wie heißen die Reisenden mit den teuersten Buchung?
select pa.vorname as "Vorname",
pa.nachname as "Nachname",
bu.preis
from buchung bu
inner join passagier pa on bu.passagier_id = pa.passagier_id
where bu.preis = (select max(preis) from buchung bu)
;

# 3. Welche Fluglinie hat die durchschnittlich teuersten Tickets?
SELECT 
    avg(sq1.preis) as "durchschnittlicher Preis",
    sq1.fluglinie_name as "Fluglinie"
FROM
(SELECT 
    b.preis,
    fl.fluglinie_name
FROM
    fluglinie fl
        INNER JOIN
    flug f ON fl.fluglinie_id = f.fluglinie_id
        INNER JOIN
    buchung b ON f.flug_id = b.flug_id) as sq1
group by sq1.fluglinie_name
order by avg(sq1.preis) desc
#limit 1
;

# 4. Welche sind die fünf Flugzeuge mit der höchsten Kapazität, die vom
# Flughafen ALTAMIRA abgeflogen sind?
SELECT 
    distinct fz.flugzeug_id,f_t.bezeichnung, fz.kapazitaet, fh.name
FROM
    flugzeug fz
        INNER JOIN
    flug f ON fz.flugzeug_id = f.flugzeug_id
        INNER JOIN
    flughafen fh ON fh.flughafen_id = f.von and fh.name = 'ALTAMIRA'
inner join flugzeug_typ f_t on fz.typ_id = f_t.typ_id
order by fz.kapazitaet desc    
;

# 5. Wie viele Personen hat die Airline Spain Airlines vom 2015-06-06
# bis zum 2015-06-08 transportiert?
SELECT 
    fl.fluglinie_name,
    count(distinct f.flug_id) as "Anzahl der Flüge",
    count(b.buchung_id) as "transportierte Personen"
FROM
    buchung b
        INNER JOIN
    flug f ON b.flug_id = f.flug_id and (f.abflug between "2015-06-06 00:00:00" and "2015-06-08 00:00:00") and f.fluglinie_id = "89"
        INNER JOIN
    fluglinie fl ON f.fluglinie_id = fl.fluglinie_id
        INNER JOIN
    passagier p ON b.passagier_id = p.passagier_id
;

# 6. Gebe für jeden Flug, die Flugnummer, die Kapazität des Flugzeuges
# und die Anzahl der Buchungen an. Füge noch eine Spalte hinzu, die
# anzeigt, ob dieser Flug mehr als 50% ausgelastet war.
SELECT 
    f.flug_id AS 'Flug',
    f.flugnr AS 'Flugnummer',
    fz.kapazitaet AS 'Kapazität des Flugzeuges',
    sq1.Anzahl_der_Buchungen,
    CASE
        WHEN sq1.Anzahl_der_Buchungen < (fz.kapazitaet / 2) THEN '< 50 % ausgelastet'
        ELSE '>= 50 % ausgelastet'
    END AS 'Auslastung'
FROM
    flug f
        INNER JOIN
    flugzeug fz ON f.flugzeug_id = fz.flugzeug_id
        INNER JOIN
    (SELECT 
        COUNT(b1.buchung_id) AS 'Anzahl_der_Buchungen', f2.flug_id
    FROM
        buchung b1
    INNER JOIN flug f2 ON b1.flug_id = f2.flug_id
    GROUP BY f2.flug_id) AS sq1 ON f.flug_id = sq1.flug_id
ORDER BY sq1.Anzahl_der_Buchungen DESC
;

# 7. Welche Fluglinie fliegt am meisten zum Flughafen KAGOSHIMA?
SELECT
	count(f.flug_id) as "Anzahl Flüge",
    f.fluglinie_id as "Fluglinien_nummer",
    fl.fluglinie_name as "Fluglinie"
    from
    flug f
        INNER JOIN
    flughafen fh ON fh.flughafen_id = f.nach
        INNER JOIN
    fluglinie fl ON f.fluglinie_id = fl.fluglinie_id
WHERE
    fh.stadt = 'KAGOSHIMA'
GROUP BY f.fluglinie_id
order by "Anzahl Flüge" desc
;

# 8. Welche Flugzeuge einer Fluglinie mit einem italienischen Flughafen
# als Basis machen die meisten Flüge und was für ein Typ sind sie?

SELECT
    fl.fluglinie_name as "Fluglinie",
    f_t.bezeichnung as "Flugzeugtyp",
    count(f.flug_id) as "Anzahl der Flüge"
FROM
    flughafen fh
    inner join fluglinie fl on fh.flughafen_id = fl.flughafen_id
    inner join flug f on fl.fluglinie_id = f.fluglinie_id
    inner join flugzeug fz on fl.fluglinie_id = fz.fluglinie_id
    inner join flugzeug_typ f_t on fz.typ_id = f_t.typ_id
WHERE
    fh.land = 'ITALY'
group by fl.fluglinie_name,f_t.bezeichnung
order by count(f_t.bezeichnung) desc
;

# 9. Wie groß sind die gesamten Anteile in Prozent aller Buchungen je
# nach Flugzeugtyp?
SELECT 
    f_t.bezeichnung AS 'Flugzeugtyp',
    (COUNT(b.buchung_id) / (SELECT 
            COUNT(buchung_id)
        FROM
            buchung)) * 100 AS 'Prozentanteile'
FROM
    buchung b
        INNER JOIN
    flug f ON b.flug_id = f.flug_id
        INNER JOIN
    flugzeug fz ON f.flugzeug_id = fz.flugzeug_id
        INNER JOIN
    flugzeug_typ f_t ON fz.typ_id = f_t.typ_id
GROUP BY f_t.bezeichnung
order by Prozentanteile desc
;
