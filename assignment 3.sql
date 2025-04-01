CREATE TABLE panya (
    id INT PRIMARY KEY,
    fullName VARCHAR(100),
    age INT,
);

INSERT INTO panya (id, fullName, age) VALUES
(1, 'John Bosco', 20),
(2, 'Amimo Smith', 22),
(3, 'Alice Wahome', 19),
(4, 'Bob Braxton', 21);


UPDATE panya
SET age = 20
WHERE id = 2;

SELECT *
FROM panya;