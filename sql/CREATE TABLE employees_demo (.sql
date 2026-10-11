CREATE TABLE employees_demo (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT
);
INSERT INTO employees_demo(id,name,department)
VALUES(1,'Sharu','IT');

CREATE TABLE departments_demo (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT
);

CREATE TABLE employee_details (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department_id INTEGER,
    FOREIGN KEY (department_id)
        REFERENCES departments_demo(department_id)
);

SELECT name
FROM sqlite_master
WHERE type = 'table';

INSERT INTO departments_demo (department_id, department_name)
VALUES (10, 'IT');

SELECT * FROM departments_demo;

INSERT INTO employee_details (id, name, department_id)
VALUES (1, 'Sharu', 10);

SELECT * FROM employee_details;

INSERT INTO employee_details (id, name, department_id)
VALUES (2, 'Arun', 99);

PRAGMA foreign_keys = ON;

INSERT INTO employee_details (id, name, department_id)
VALUES (3, 'Priya', 99);

PRAGMA foreign_keys;

PRAGMA foreign_keys = ON;

PRAGMA foreign_keys;

CREATE TABLE employee_email_demo (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT UNIQUE
);

INSERT INTO employee_email_demo
VALUES(1,'Sharu','sharu@example.com');

SELECT * FROM employee_email_demo;

INSERT INTO employee_email_demo (id, name, email)
VALUES (2, 'Arun', 'sharu@example.com');

SELECT * FROM employee_email_demo;

SELECT sql
FROM sqlite_master
WHERE type = 'table'
AND name = 'employee_email_demo';

CREATE TABLE employee_phone_demo (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT
);

INSERT INTO employee_phone_demo (id, phone)
VALUES (1, '9876543210');

CREATE TABLE employee_status_demo (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    status TEXT DEFAULT 'Active'
);

INSERT INTO employee_status_demo(id,name)
VALUES(1,'Sharu');

SELECT * FROM employee_status_demo;

CREATE TABLE employee_age_demo (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER CHECK (age >= 18)
);

INSERT INTO employee_age_demo (id, name, age)
VALUES (1, 'Sharu', 24);


INSERT INTO employee_age_demo (id, name, age)
VALUES (2, 'Arun', 15);
