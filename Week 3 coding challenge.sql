CREATE TABLE teacher (
    student_id INT PRIMARY KEY,
    Full_Name VARCHAR (100) NOT NULL,
    Age INT,
    date_of_birth DATE,
    Gender VARCHAR(100),
    gpa DECIMAL(3,2),
);

select *
FROM teacher;

ALTER TABLE teacher
DROP COLUMN gpa;

INSERT INTO teacher (student_id, Full_Name, Age, Gender) VALUES
    ('1', 'Johnson Sakaja', '38', 'Male'),
    ('2', 'Williams Serena', '47', 'Female'),
    ('3', 'Brown Mauzo', '37', 'Male');


SELECT * 
FROM teacher;

ALTER TABLE teacher
DROP COLUMN date_of_birth;

INSERT INTO teacher (student_id, Full_Name, Age, Gender) VALUES
('4', 'Levi Kalama', '22', 'Male')


INSERT INTO teacher (student_id, Full_Name, Age, Gender) VALUES
('5', 'JKINS Limited', '24', 'Gay')

SELECT *
FROM teacher;