create database sql_triggers;
show databases;
use sql_triggers;
show tables;

#Before Insert Trigger
create table customers
(cust_id int, age int, name varchar(50));

truncate table customers;
select * from customers;

delimiter //
create trigger age_verify
Before insert
on customers for each row
if new.age < 0 then set new.age = 0;
end if; //

insert into customers
values (101, 27, "James"),
(102, -40, "Ammy"),
(103, 32, "Ben"),
(104,-39, "Angela");

select * from customers;


#After INSERT trigger
# Fire a trigger if birthday column as null value in customer1 table and give message
create table customer1(
id int auto_increment primary key,
name varchar(40) not null,
email varchar(30), birthdate date);

create table message ( 
id int auto_increment,
messageId int,
message varchar(300) not null,
primary key(id, messageId));


#After INSERT trigger command
Delimiter //
create trigger check_null_dob
After insert
on customer1 for each row
begin
if new.birthdate is null then
insert into message (messageId, message)
values (new.id,concat('Hi ', new.name,', Please, update your date of birth'));
end if;
end //

insert into customer1 (name, email, birthdate)
values ("Nancy", "nancy@abc.com", NULL),
("Ronald","ronald@xyz.com", "1998-11-16"),
("Chris", "chris@xyz.com","1997-08-20"),
("Alice", "alice@anc.com", NULL);

select * from message;

# Before UPDATE  trIGGER3
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

delimiter //
create trigger upd_trigger
before update
on employees for each row
begin
if new.salary=10000 then set new.salary = 85000;
elseif new.salary < 10000 then set new.salary = 72000;
end if;
end //
delimiter ;

SET SQL_SAFE_UPDATES = 0;
update employees
set salary = 8000;
SET SQL_SAFE_UPDATES = 1;

SELECT * FROM employees;
select * from employees;


# After Update TRIGGER
create table employees1
(emp_id int primary key,
emp_name varchar(25),age int, salary float);

insert into employees1 values
(101, "Jimmy", 35, 70000),
(102, "Shane", 30, 55000),
(103, "Маrrу", 28, 62000),
(104, "Dwayne", 37, 57000),
(105, "Sara", 32, 72000),
(106, "Ammy", 35, 80000),
(107, "Jack", 40, 100000);

#Whenever someone’s salary is updated, the trigger will automatically record the old and new salaries in another table called salary_audit.

CREATE TABLE salary_audit (
emp_id int,
old_salary FLOAT,
new_salary FLoat,
changed_on datetime
);

Delimiter //
create trigger after_salary_update
AFTER UPDATE
ON employees1 for each row
begin
IF new.salary <> old.salary then
INSERT INTO salary_audit(emp_id, old_salary, new_salary, changed_on)
VALUES (old.emp_id, old.salary, NEW.salary,NOW());
end if;
end; //

delimiter ;

update employees1
SET salary = 90000
Where emp_id = 106;

select * from salary_audit;

# Before DELETE TRIGGER

create TABLE Salary (
old int primary key,
validfrom date not null,
amount float not null);

insert into Salary (old, validfrom, amount)
values(101,'2005-05-01',55000),
(102,'2007-08-01',68000),
(103,'2006-09-01',75000);

select * from salary;

#DROP TRIGGER salary_delete;
create table salarydel1 (
id int primary key auto_increment,
old int, validfrom date not null, amount float,
deletedat timestamp default now());

delimiter $$
create trigger salary_delete
before delete
on Salary FOR EACH ROW
BEGIN
insert into Salarydel1(old,validfrom, amount)
VALUES(OLD.old, old.validfrom,old.amount);
end $$

delimiter ;

DELETE FROM Salary
where old = 103;
 
Select * from Salarydel1;