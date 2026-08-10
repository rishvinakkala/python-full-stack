create database collageDB;
use collageDB;

CREATE TABLE Student (
    Student_ID INT PRIMARY KEY,
    Student_Name VARCHAR(50),
    Gender VARCHAR(10),
    Age TINYINT,
    Phone_Number VARCHAR(15),
    Course_ID INT
);

INSERT INTO Student
VALUES
(1, 'Ravi', 'Male', 20, '9876543210', 101),
(2, 'Priya', 'Female', 19, '9123456780', 102),
(3, 'Arjun', 'Male', 21, '9012345678', 104),
(4, 'Sneha', 'Female', 22, '9988776655', 105),
(5, 'Kiran', 'Male', 20, '9876501234', 103);

select *from student;

CREATE TABLE Course (
    Course_ID INT PRIMARY KEY,
    Course_Name VARCHAR(50)
);

INSERT INTO Course
VALUES
(101, 'BCA'),
(102, 'B.Com'),
(103, 'B.Sc'),
(104, 'MCA'),
(105, 'MBA');

select *from course;

SELECT *FROM Student
INNER JOIN Course
ON Student.Course_ID = Course.Course_ID;

SELECT 
Student.student_id,
course.course_name
from student
cross join course;


show databases;
use collageDB;

CREATE TABLE teacher(
  teacher_ID int primary key,
  teacher_name varchar(100),
  techer_subject varchar(50)
  );

select *from teacher;

insert into teacher values
(101,"harsh","java"),
(102,"kiran","python"),
(103,"hyma","accounts");

select *from teacher;
use collageDb;

create table student_details(
    student_name varchar(50),
    student_course varchar(15)
);

