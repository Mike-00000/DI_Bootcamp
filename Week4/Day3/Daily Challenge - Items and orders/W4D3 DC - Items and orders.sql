-- Daily Challenge : Items & Orders

-- 1 and 2

-- CREATE SEQUENCE mysequence
-- INCREMENT 1
-- START 1;

-- CREATE TABLE product_orders
-- (
-- 	product_orders_id   INTEGER NOT NULL DEFAULT nextval('mysequence') PRIMARY KEY,
--    	fname_customer   CHAR(30) NOT NULL,
--    	lname_customer   CHAR(30) NOT NULL,
-- 	quantity_order	INTEGER DEFAULT 1
-- );

-- CREATE TABLE items
-- (
--    	items_id   INTEGER PRIMARY KEY,
-- 	items_name   CHAR(30) NOT NULL,
-- 	items_size   INT NOT NULL,
-- 	items_price DECIMAL,
-- 	profile_orders_id   INTEGER REFERENCES product_orders (product_orders_id)
-- );

-- INSERT INTO product_orders(fname_customer, lname_customer, quantity_order)
-- VALUES
-- ('Jose', 'Garcia', 2),
-- ('Franck', 'Dubosc', 8),
-- ('Jim', 'Carrey', 1),
-- ('Charlie', 'Chaplin', 5);

-- INSERT INTO items(items_id, items_name, items_size, items_price)
-- VALUES
-- (1, 'Tee_Shirt', 2, 49.90)

-- SELECT * FROM product_orders
-- SELECT * FROM items

-- ALTER TABLE product_orders
-- ADD total_price DECIMAL DEFAULT 0


-- 3
SELECT product_orders_id, items_price, product_orders.quantity_order
FROM product_orders
JOIN items ON product_orders.product_orders_id = items.profile_orders_id
WHERE total_price = items.items_price * product_orders.quantity_order







