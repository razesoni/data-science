use schooldb;
select name, age, date_of_birth from student where grade="12th";
select * from student where name not like '%sh' order by age asc limit 2;