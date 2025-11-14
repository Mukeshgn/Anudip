create database sql_intro;
show databases;
use sql_intro;

create table emp_details (Name varchar(25), Age int, Gender char(1), doj date, city varchar(15), salary float);
describe emp_details;

insert into emp_details
values("Jimmy", 35, "M", "2005-05-30", "Chicago", 70000),
("Shane",30,"M","1999-06-25","Seattle",55000),
("Marry", 28,"F","2009-03-10", "Boston", 62000),
("Dwayne", 37, "M", "2011-07-12", "Austin", 57000),
("Sara", 32, "F", "2017-10-27", "New York", 72000),
("Army", 35, "F", "2014-12-20", "Seattle", 80000);

select * from emp_details;

select distinct city from emp_details;

select count(name) from emp_details;

select count(name) as count_name from emp_details;

select sum(salary) from emp_details;

select name, age, city from emp_details;

select * from emp_details where age > 30;

select Name, Gender, city from emp_details where Gender = "F";

select * from emp_details where city = 'Chicago' or city = 'Austin';

select * from emp_details where city in('Chicago','Austin');

select * from emp_details where doj between "2000-01-01" and "2010-12-31";

select * from emp_details where age>30 and Gender ='M';

select Gender, sum(salary) as total_salary from emp_details
group by Gender;

select * from emp_details order by salary;

select * from emp_details order by salary desc;

select (10+20) as addition;

select length("India") as total_len;

select repeat('@',10);

select upper("India");
select lower("INSIA");

select curdate();

select day(curdate());

select now();

#String functions
select upper("India") as upper_case;
select ucase("India") as upper_case;
select lower("India") as lower_case;
select lcase("India") as lower_case;

#length of string
select character_length('India') as total_len;

#in table
select name, character_length(name) as total_len from emp_details;
select name, char_length(name) as total_len from emp_details;
select name, length(name) as total_len from emp_details;

#Concatenate
select concat("India"," is"," in Asia.") as concatenated;
select name, concat(name," ",age) as name_age from emp_details;

#reverse
select reverse("India");
select name, reverse(name) from emp_details;

#replace 
select replace('Orange is a vegetable','vegetable','fruit');

#trim
select length("        India           ");
select ltrim("        India           ");
select length(ltrim("        India           "));
select length(rtrim("        India           "));
select length(trim("        India           "));

#position function
select position("Nandh" in "Mukesh Gopi Nandh");

#ASCII
select ascii("a");
select ascii(4);