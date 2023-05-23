
-- 🌟 Exercise 1: DVD Rental
-- 1
-- SELECT name FROM language

-- 2.1
-- SELECT title, description, name
-- FROM film
-- JOIN language ON film.language_id = language.language_id
-- ORDER BY title


-- 2.2
-- SELECT film.title, film.description, language.name
-- FROM language
-- LEFT JOIN film ON film.language_id = language.language_id
-- ORDER BY language.name;


-- 3
-- CREATE TABLE new_film (
--     newfilm_id INT PRIMARY KEY,
--     title VARCHAR(255)
-- );

-- INSERT INTO new_film(newfilm_id, title)
-- VALUES 
-- (1, 'Matrix'),
-- (2, 'Avalon'),
-- (3, 'Avatar'),
-- (4, 'Split');

-- 4
-- CREATE TABLE customer_review (
--     review_id SERIAL PRIMARY KEY,
--     film_id INT,
--     language_id INT,
--     title VARCHAR(255),
--     score INT,
--     review_text TEXT,
--     last_update TIMESTAMP,
--     FOREIGN KEY (film_id) REFERENCES new_film(newfilm_id) ON DELETE CASCADE,
--     FOREIGN KEY (language_id) REFERENCES language(language_id)
-- );

-- 5
-- INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)
-- VALUES (1, 2, 'Incredible movie!', 10, 'A philosophical science-fiction movie', NOW());

-- INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)
-- VALUES (1, 2, 'Impressive movie!', 9, 'An ecologic science-fiction movie', NOW());

-- 6
-- DELETE FROM new_film
-- WHERE newfilm_id = 1;

-- SELECT * FROM customer_review



-- 🌟 Exercise 2 : DVD Rental
-- 1
-- UPDATE film
-- SET language_id = 3
-- WHERE film_id IN (1, 2, 3);

-- UPDATE film
-- SET language_id = 5
-- WHERE film_id IN (4, 5);


-- 2
-- store_id and address_id

-- 3
-- DROP TABLE customer_review;
-- It seems to be an easy step (Query returned successfully in 496 msec)

-- 4
-- SELECT COUNT(*) AS outstanding_rentals
-- FROM rental
-- WHERE return_date IS NULL;

-- 5
-- SELECT film.film_id, film.title, film.replacement_cost
-- FROM film
-- JOIN inventory ON film.film_id = inventory.film_id
-- LEFT JOIN rental ON inventory.inventory_id = rental.inventory_id
-- WHERE rental.return_date IS NULL
-- ORDER BY film.replacement_cost DESC
-- LIMIT 30;

-- 6.1
-- SELECT film.film_id, film.title, film.description, film_actor.actor_id, actor.first_name, actor.last_name
-- FROM film
-- JOIN film_actor ON film.film_id = film_actor.film_id
-- LEFT JOIN actor ON film_actor.actor_id = actor.actor_id
-- WHERE actor.first_name = 'Penelope' AND actor.last_name = 'Monroe' AND film.description ILIKE '%wrestler%';

-- 6.2
-- SELECT f.title, f.rating, f.length, category.name
-- FROM film as f
-- JOIN film_category ON film_category.film_id = f.film_id
-- -- INNER JOIN film_category;
-- JOIN category ON film_category.category_id = category.category_id
-- WHERE f.length < 60
-- AND f.rating = 'R'
-- AND category.name ILIKE 'documentary';

-- 6.3
-- SELECT film.title, customer.first_name, customer.last_name, payment.amount, rental.return_date
-- FROM film
-- JOIN inventory ON inventory.film_id = film.film_id
-- JOIN rental ON rental.inventory_id = inventory.inventory_id
-- JOIN customer ON customer.customer_id = rental.customer_id
-- JOIN payment ON payment.customer_id = customer.customer_id
-- WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan'
-- AND payment.amount > 4
-- AND rental.return_date BETWEEN '2005-07-28' AND '2005-08-01'

-- 6.4
-- SELECT film.title, film.replacement_cost, customer.first_name, customer.last_name, film.description
-- FROM film
-- JOIN inventory ON inventory.film_id = film.film_id
-- JOIN rental ON rental.inventory_id = inventory.inventory_id
-- JOIN customer ON customer.customer_id = rental.customer_id
-- WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan'
-- AND (film.description ILIKE '%boat%' OR film.title ILIKE '%boat%')
-- AND film.replacement_cost > 15
