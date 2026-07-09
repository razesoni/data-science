-- insert into students2 (id, name, age, email, adm_dt) values (2, "Akash", 20, "razesoni@gmail.com", "2023-02-28");
-- select * from students2

-- select @@autocommit

start transaction;
update students2 set age = age + 1 where id = 2;
commit;
rollback;
select * from students2