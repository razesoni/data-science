-- select current_timestamp();
-- select localtimestamp()

alter table students2 add column date_joined datetime default (now());
select * from students2