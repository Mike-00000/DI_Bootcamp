-- CREATE TABLE students (
--     students_id SERIAL PRIMARY KEY,
--     first_name VARCHAR(100) NOT NULL,
--     last_name VARCHAR(100) NOT NULL,
--     date_birth DATE NOT NULL
-- )

-- INSERT INTO students (first_name, last_name, date_birth)
-- VALUES 
-- ('Marc', 'Benichou', '1998-11-02'),
-- ('Yoan', 'Cohen', '2010-12-03'),
-- ('Lea', 'Benichou', '1987-07-27'),
-- ('David', 'Grez', '1996-04-07'),
-- ('Melanie', 'Johnson', '2003-06-14'),
-- ('Omer', 'Simpson', '1980-10-03')

-- INSERT INTO students (first_name, last_name, date_birth)
-- VALUES 
-- ('Michael', 'Touitou', '1979-10-12')

-- INSERT INTO students (first_name, last_name, date_birth)
-- VALUES 
-- ('Leah', 'Chelly', '1989-12-12')

-- SELECT * FROM students
-- SELECT first_name, last_name FROM students
-- SELECT first_name, last_name FROM students WHERE students_id = 2
-- SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' AND first_name = 'Marc'
-- SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' OR first_name = 'Marc'
-- SELECT first_name, last_name FROM students WHERE first_name LIKE '%a%'
-- SELECT first_name, last_name FROM students WHERE first_name LIKE '%a'
-- SELECT first_name, last_name FROM students WHERE first_name LIKE '%a_'
-- SELECT first_name, last_name FROM students WHERE students_id BETWEEN 1 AND 3
-- SELECT * FROM students WHERE date_birth >= '2000/01/01'