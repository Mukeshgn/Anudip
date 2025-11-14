create database sql_store_procedure;
use sql_store_procedure;

CREATE TABLE players (
    player_id INT PRIMARY KEY,
    name VARCHAR(50),
    country VARCHAR(50),
    goals INT
);

INSERT INTO players (player_id, name, country, goals)
VALUES
(101, 'Sam', 'USA', 6),
(103, 'Daniel', 'England', 7),
(104, 'Anthony', 'France', 10),
(102, 'Bruno', 'Sweden', 6),
(105, 'Alex', 'Wales', 5),
(106, 'Matt', 'Scotland', 3);


delimiter $$
create procedure top_player()
begin
select name, country, goals 
from players where goals>6;
End $$
 delimiter ;
 
 call top_player();
 
 create table employees
(emp_id int primary key,
emp_name varchar(25),age int, salary float);

insert into employees values
(101, "Jimmy", 35, 70000),
(102, "Shane", 30, 55000),
(103, "Маrrу", 28, 62000),
(104, "Dwayne", 37, 57000),
(105, "Sara", 32, 72000),
(106, "Ammy", 35, 80000),
(107, "Jack", 40, 100000);

Delimiter //
create procedure sortBySalary(IN var int)
begin
select Emp_name, age, salary from employees
order by Salary desc limit  var;
end //
delimiter ;

call sortBySalary(3);
call sortBySalary(5);

#drop procedure update_salary;
# UPDATE 
delimiter ??
create procedure update_salary (IN temp_name varchar(20), 
in new_salary float)
begin
update employees set 
salary = new_salary where emp_name = temp_name;
end; ??
delimiter ;

select * from employees;
set sql_safe_updates = 0;
call update_salary("Маrrу", 80000);
set sql_safe_updates = 1;

select * from employees;


# Store Procedure using OUT parameter

#DROP Procedure sp_countEmployees;
delimiter //
create procedure sp_countEmployees(OUT Total_Emps int)
Begin
Select count(EMP_name) into Total_Emps from employees 
where age > 32;
end //
delimiter ;

call sp_countEmployees(@C_emp);
select @C_emp as Count_employess_32;



#Trigger in SQL

create table student(
st_roll int, age int, name varchar(50), marks float);

delimiter //
create trigger mark_verify
before insert 
on student for each row
begin
if new.marks < 0 then set new.marks = 50;
end if;
end; //

delimiter ;

insert into student(st_roll,age,name,marks) 
values(501,10,'Ruth',75.0),
(502,12,'Mike',-20.5),
(503,13,'Dave',90.0),
(504,10,'Jacobs',-12.5);

Select * from Student;
