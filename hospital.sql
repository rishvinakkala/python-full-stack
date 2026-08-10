CREATE DATABASE hospitalDB;
USE hospitalDB;
CREATE TABLE Patient (
    Patient_ID INT PRIMARY KEY AUTO_INCREMENT,
    First_Name VARCHAR(50),
    Last_Name VARCHAR(50),
    Gender VARCHAR(10),
    DOB DATE,
    Phone VARCHAR(15),
    Address VARCHAR(100),
    Blood_Group VARCHAR(5)
);

CREATE TABLE Doctor (
     Doctor_ID INT PRIMARY KEY AUTO_INCREMENT,
     Doctor_Name VARCHAR(100),
     Specialization VARCHAR(50),
     Phone VARCHAR(100),
     Email VARCHAR(100),
     Experience INT
);


SELECT *FROM Doctor ;     

CREATE TABLE Appointment (
      Appoinment_ID INT PRIMARY KEY AUTO_INCREMENT,
      Patient_ID INT,
      Doctor_ID INT,
      Appointment_Date DATE,
      Appointment_Time TIME,
      Satus VARCHAR(20),
      FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID),
      FOREIGN KEY (Doctor_ID) REFERENCES Doctor(Doctor_ID)
);

SELECT *FROM Appointment;

DESC Patient;

SHOW TABLES;


INSERT INTO Patient VALUES 
(123,'KUMAR','SAI','MALE','2000-4-12','9887654392','XYZ COLONY','B+');
INSERT INTO patient VALUES
(234,'RAMESH','REDDY','MALE','2008-7-17','9876545673','YZT COLONY','A-');

SELECT *FROM Patient;

SELECT First_name,Blood_Group 
FROM Patient;

SELECT *FROM Patient WHERE Blood_Group='A-';

UPDATE Patient SET Gender='FEMALE' WHERE Patient_ID=234;

DESC Patient;

SELECT *FROM Patient;

ALTER TABLE patient
ADD Diesease VARCHAR(100);

ALTER TABLE Patient 
MODIFY age TINYINT;


RENAME TABLE Appointment TO Consult;


describe patient;

SELECT *FROM patient;

UPDATE Patient 
SET diesease = 'BP'
WHERE Patient_ID=123;


UPDATE Patient
SET diesease = 'diabate'
WHERE Patient_ID=234;