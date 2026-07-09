-- create database schoolDB; 

-- use schoolDB;

-- create table student(
-- id int primary key,
-- name varchar(100),
-- age int,
-- grade varchar(10),
-- date_of_birth date
-- );

-- insert into student(id, name, age, grade, date_of_birth)
-- value(1, "Akash", 20, "12th", "2004-12-25")

insert into student(id, name, age, grade, date_of_birth) values
(2, "JOhn", 20, "10th", "2006-01-23"),
(3, "Mary", 18, "10th", "2008-02-29");

select * from student
