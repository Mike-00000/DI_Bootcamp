-- CREATE TABLE items(
--  	items_id SERIAL PRIMARY KEY,
--  	name_items VARCHAR (100) NOT NULL,
--  	price SMALLINT NOT NULL DEFAULT 0
-- 	)

-- DROP TABLE IF EXISTS items;

-- CREATE TABLE customers (
--     customers_id SERIAL PRIMARY KEY,
--     first_name VARCHAR(100) NOT NULL,
--     last_name VARCHAR(100) NOT NULL
-- 	)


-- INSERT INTO customers (first_name, last_name)
-- VALUES 
-- ('Greg', 'Jones'),
-- ('Sandra', 'Jones'),
-- ('Scott', 'Scott'),
-- ('Trevor', 'Green'),
-- ('Melanie', 'Johnson')


-- INSERT INTO items (name_items, price)
-- VALUES 
-- ('Small Desk', 100),
-- ('Large Desk', 300),
-- ('Fan', 80)


-- SELECT * FROM items

-- SELECT * FROM items WHERE price > 80
-- SELECT * FROM items WHERE price <= 300

-- SELECT * FROM customers WHERE last_name like '%Smith%'
-- SELECT * FROM customers WHERE last_name like '%Jones%'
-- SELECT * FROM customers WHERE NOT first_name like '%Scott%'



