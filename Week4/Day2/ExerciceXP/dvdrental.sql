-- 1
-- SELECT * FROM customer

-- 2
-- SELECT Concat(Concat(first_name, ' '), last_name) AS full_name FROM customer;

-- 3
-- SELECT DISTINCT create_date FROM customer

-- 4
-- SELECT * FROM customer ORDER BY first_name ASC

-- 5
-- SELECT film_id, title, description, release_year,rental_rate 
-- FROM film ORDER BY rental_rate ASC

-- 6
-- SELECT first_name, last_name, address, phone, district
-- FROM customer
-- FULL JOIN address ON customer_id = customer_id
-- WHERE district = 'Texas'

-- 7
-- SELECT description FROM film WHERE film_id BETWEEN 15 AND 150

-- 8
-- SELECT film_id, title, description, length, rental_rate FROM film WHERE title = 'Matrix'

-- 9
-- SELECT film_id, title, description, length, rental_rate FROM film WHERE title ILIKE 'Ma%' 

-- 10
-- SELECT replacement_cost, title FROM film ORDER BY replacement_cost ASC LIMIT 10

-- 11
-- SELECT replacement_cost, title FROM film ORDER BY replacement_cost ASC OFFSET 10 FETCH NEXT 10 ROWS ONLY;

-- 12
-- SELECT first_name, last_name, amount, payment_date
-- FROM customer
-- JOIN payment ON customer.customer_id = payment.customer_id
-- ORDER BY customer.customer_id;

-- 13
-- SELECT film.*
-- FROM film
-- LEFT JOIN inventory ON film.film_id = inventory.film_id
-- WHERE inventory.film_id IS NULL;

-- 14
-- SELECT city.city, country.country
-- FROM city
-- JOIN country ON city.country_id = country.country_id ORDER BY country.country_id ASC

-- 15
-- SELECT c.customer_id, c.first_name || ' ' || c.last_name AS full_name, p.amount, p.payment_date
-- FROM customer c
-- JOIN payment p ON c.customer_id = p.customer_id
-- JOIN staff s ON p.staff_id = s.staff_id
-- ORDER BY s.staff_id;
