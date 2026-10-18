
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INTEGER,
    course VARCHAR(100),
    marks INTEGER
);

INSERT INTO students (name, age, course, marks)
VALUES ('Sharu', 24, 'Python', 85);

SELECT * FROM students;