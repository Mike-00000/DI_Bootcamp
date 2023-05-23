-- Daily Challenge: Tables Relationships
-- Part 1
-- 1

-- CREATE SEQUENCE mysequence
-- INCREMENT 1
-- START 1;

-- CREATE TABLE customer
-- (
-- 	customer_id   INTEGER NOT NULL DEFAULT nextval('mysequence') PRIMARY KEY,
--    	first_name   CHAR(30) NOT NULL,
--    	last_name   CHAR(30) NOT NULL
-- );

-- CREATE TABLE profile
-- (
--    	profile_id   INTEGER PRIMARY KEY,
--    	isLoggedIn BOOLEAN DEFAULT false,
--    	profile_cust_id   INTEGER REFERENCES customer (customer_id)
-- );


-- 2
-- INSERT INTO customer(first_name, last_name)
-- VALUES
-- ('John', 'Doe'),
-- ('Jerome', 'Lalu'),
-- ('Lea', 'Rive');


-- 3
-- Insert John's customer profile
-- Insert John's customer profile
-- INSERT INTO profile (profile_id, isLoggedIn, profile_cust_id)
-- VALUES (1, true, (SELECT customer_id FROM customer WHERE first_name = 'John' AND last_name = 'Doe'));

-- -- Insert Jerome's customer profile
-- INSERT INTO profile (profile_id, isLoggedIn, profile_cust_id)
-- VALUES (2, false, (SELECT customer_id FROM customer WHERE first_name = 'Jerome' AND last_name = 'Lalu'));


-- 4
-- SELECT customer.first_name, profile.isloggedin
-- FROM profile
-- JOIN customer ON profile.profile_id = customer.customer_id


-- SELECT customer.first_name, profile.isloggedin
-- FROM profile
-- FULL JOIN customer ON profile.profile_id = customer.customer_id


-- SELECT customer.first_name, profile.isloggedin
-- FROM profile
-- JOIN customer ON profile.profile_id = customer.customer_id
-- WHERE isloggedin is true

