# 1. Gib die Namen aller Mitarbeitenden und deren Titel aus.
select
lastName as "Nachname",
firstName as "Vorname",
jobTitle as "Titel"
from employees
;

#2. Gib alle Produktinformationen für die Produktlinie Motorcycles aus.
select
*
from products
where productLine = "Motorcycles"
;

# 3. Wie viele Motorräder haben wir noch auf Lager?
select
sum(quantityInStock)
from products
where productLine = "Motorcycles"
;

# 4. Wie viel kostet das günstigste, das teuerste und wie viel ein
# durchschnittliches Motorrad?
select
#productCode,
min(productName),
min(buyPrice) as "günstigstes Motorrad",
max(buyPrice) as "teuerstes Motorrad",
avg(buyPrice) as "Preis durchschnittliches Motorrad"
from products
where productLine = "Motorcycles"
;

# 5. Gibt es Bestellungen, die später versandt wurden als gefordert?
select * from orders
where requiredDate < shippedDate
;

# 6. Was sind die 3 häufigsten Kommentare einer Bestellung?
select
comments,
count(comments)
from orders
group by comments
having comments = comments
order by count(comments) desc
;

# 7. Wie lange benötigen unsere Produkte durchschnittlich vom
# Eingang der Bestellung bis zur Auslieferung? Benutze hierfür
# keine Subtraktion, sondern die Funktion datediff!
select
avg(datediff(shippedDate,orderDate)) as "durchschnittliche Auslieferungszeit in Tagen"
from orders
;

# -------------------Komplexere Queries----------------------

# 8. Welches Sales-Mitglied bringt am meisten Umsatz (pm.amount) rein?
select
e.employeeNumber,
e.firstName,
e.lastName,
sum(pm.amount) as "Umsatz"
from employees e
inner join customers c on e.employeeNumber = c.salesRepEmployeeNumber
inner join payments pm on c.customerNumber = pm.customerNumber
group by e.employeeNumber
having e.employeeNumber = e.employeeNumber
order by sum(pm.amount) desc
limit 1
;

# 9. Gibt es Produkte, die keiner bestellt hat?
select
p.productCode,
sum(od.quantityOrdered)
from orderdetails od
right join products p on od.productCode = p.productCode
where od.productCode is null
group by p.productCode
;

# 10. Liste alle unterschiedlichen Porsches, die Verkaufsmenge, den
# erwarteten Umsatz aus dem MSRP und den erzeugten Umsatz
#  aus dem Verkaufspreis auf.
SELECT 
    p.productName,
    SUM(od.quantityOrdered) AS 'Bestellmenge',
    SUM((p.MSRP - p.buyPrice) * od.quantityOrdered) AS 'Erw. Umsatz',
    SUM((od.priceEach - p.buyPrice) * od.quantityOrdered) AS 'Umsatz'
FROM
    orderdetails od
        INNER JOIN
    products p ON p.productCode = od.productCode
WHERE
    p.productName LIKE '%Porsche%'
GROUP BY p.productName
;

# -----------------Aufgaben mit Subqueries-------------------------

# 11. Was ist der Umsatz pro Kunde in Total und in % vom Gesamtumsatz?
select
c.customerNumber,
sum(pm.amount) as "Ausgaben pro customerNumber",
sum(pm.amount) / (select sum(amount) from payments) as "Anteil Umsatz Kunde am Gesamtumsatz"
from customers c
inner join payments pm on c.customerNumber = pm.customerNumber
group by c.customerNumber
;

# 12. Was ist der durchschnittliche Pro-Kopf-Umsatz ( ) in den 𝑝𝑚.𝑎𝑚𝑜𝑢𝑛𝑡
# 𝐴𝑛𝑧𝑎ℎ𝑙 𝑀𝐴 einzelnen Standorten?
SELECT 
    o.city,
    o.country,
    COUNT(e.employeeNumber) AS 'MA',
    prof.Profit AS 'Profit',
    prof.Profit / COUNT(e.employeeNumber) AS 'PKP'
FROM
    employees e
        INNER JOIN
    offices o ON e.officeCode = o.officeCode
        INNER JOIN
    (SELECT 
        o.city, SUM(pm.amount) AS 'Profit'
    FROM
        payments pm
    INNER JOIN customers c ON pm.customerNumber = c.customerNumber
    INNER JOIN employees e ON c.salesRepEmployeeNumber = e.employeeNumber
    INNER JOIN offices o ON e.officeCode = o.officeCode
    GROUP BY o.city) AS prof ON o.city = prof.city
GROUP BY o.officeCode
;

# 13. Vergleiche den Umsatz von den einzelnen Monaten in 2003 mit
# den Monaten 2004 und erstelle die Differenz.
select
month(o.orderDate) as "Monate",
y2003.Umsatz_2003,
sum(od1.quantityOrdered * od1.priceEach) as "Umsatz_2004",
sum(od1.quantityOrdered * od1.priceEach) - y2003.Umsatz_2003 as "Differenz"

from
orderdetails od1
inner join orders o on od1.orderNumber = o.orderNumber
inner join (select
			sum(od2.quantityOrdered * od2.priceEach) as "Umsatz_2003",
            month(o.orderDate) as "Monat_2003",
            year(o.orderDate) as "Jahr_2003"
            from orderdetails od2
            inner join orders o on od2.orderNumber = o.orderNumber
            where year(o.orderDate) = "2003"
            group by year(o.orderDate),month(o.orderDate)) as y2003 on month(o.orderDate) = y2003.Monat_2003

where year(o.orderDate) = "2004"
group by month(o.orderDate),year(o.orderDate),y2003.Monat_2003,y2003.Jahr_2003

;

# 14. Welches Paar von Produkten wird häufig zusammen gekauft?
select
od1.productCode as "Item 1",
od2.productCode as "Item 2",
count(od1.orderNumber)
from
orderdetails od1
inner join orderdetails od2 on od1.productCode < od2.productCode and od1.orderNumber = od2.orderNumber
group by od1.productCode,od2.productCode
order by count(od1.orderNumber) desc
;

# 15. Gibt es Produkte, die wir im Dezember 2003 verkauft haben, aber nicht im Dezember 2004?
select
    res2003.productCode,
    res2003.c2003,
    res2004.c2004
from
    (select
        od.productCode,
        count(*) as c2003
    from orders o
    inner join orderdetails od on o.orderNumber = od.orderNumber
    where orderDate like '2003-12%'
    group by od.productCode) res2003

left join
    (select
        od.productCode,
        count(*) as c2004
    from orders o
    inner join orderdetails od on o.orderNumber = od.orderNumber
    where orderDate like '2004-12%'
    group by od.productCode) res2004
    on res2003.productCode = res2004.productCode and res2004.productCode is null

group by productCode
;

# 16. Berechne den durchschnittlichen Wert aller Bestellungen in 2004.
SELECT 
    AVG(sq.summe)
FROM
    (SELECT 
        SUM(od.priceEach * od.quantityOrdered) AS 'summe'
    FROM
        orderdetails od
    INNER JOIN orders o ON od.orderNumber = o.orderNumber
        AND YEAR(o.orderDate) = '2004'
    GROUP BY od.orderNumber) AS sq
;

#17. Welcher Bestellungswert von 2004 ist höher als der ausgerechnete Wert von Aufgabe 16?
SELECT 
    orderNumber,
    SUM(quantityOrdered * priceEach) AS 'Bestellwert'
FROM
    orderdetails
GROUP BY orderNumber
HAVING (SUM(quantityOrdered * priceEach)) > (SELECT 
        AVG(sq.summe)
    FROM
        (SELECT 
            SUM(od.priceEach * od.quantityOrdered) AS 'summe'
        FROM
            orderdetails od
        INNER JOIN orders o ON od.orderNumber = o.orderNumber
            AND YEAR(o.orderDate) = '2004'
        GROUP BY od.orderNumber) AS sq)
ORDER BY Bestellwert
;
