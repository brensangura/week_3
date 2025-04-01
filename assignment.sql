CREATE TABLE student (
    id INT PRIMARY KEY,
    fullName VARCHAR(100),
    age INT,
);

#creates the student table with three columns: id, fullName, and age.

INSERT INTO student (id, fullName, age) VALUES
(1, 'John Bosco', 20),
(2, 'Amimo Smith', 22),
(3, 'Alice Wahome', 19),
(4, 'Bob Braxton', 21);

#inserts four records into the student table with their respective id, fullName, and age.

UPDATE student
SET age = 20
WHERE id = 2;

#updates the age of the student with id 2 to 20.