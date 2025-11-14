#Sub query using SELECT statement
show databases;
create database sql_subqueries;
show databases;
use sql_subqueries;
create table employees (Emp_Id int primary key, Emp_Name varchar(25),
Age int, Gender char(1), Doj date, Dept varchar(20), City varchar(20),
Salary float);

#show table description
describe employees;

CREATE TABLE Employees1 (
    Emp_Id INT PRIMARY KEY,
    Emp_Name VARCHAR(50),
    Age INT,
    Gender CHAR(1),
    Doj DATE,
    Dept VARCHAR(50),
    City VARCHAR(50),
    Salary INT
);

INSERT INTO employees1 (Emp_Id, Emp_Name, Age, Gender, Doj, Dept, City, Salary) VALUES
(101, 'Jimmy', 35, 'M', '2005-05-30', 'Sales', 'Chicago', 70000),
(102, 'Shane', 30, 'M', '1999-06-25', 'Marketing', 'Seattle', 55000),
(103, 'Marry', 28, 'F', '2009-03-10', 'Product', 'Boston', 62000),
(104, 'Dwayne', 37, 'M', '2011-07-12', 'Tech', 'Austin', 57000),
(105, 'Sara', 32, 'F', '2017-10-27', 'Sales', 'New York', 72000),
(106, 'Ammy', 35, 'F', '2014-12-20', 'IT', 'Seattle', 80000),
(107, 'Jack', 40, 'M', '2012-07-14', 'Finance', 'Houston', 100000),
(108, 'Angela', 36, 'F', '2007-02-04', 'Tech', 'New York', 110000),
(109, 'Marcus', 25, 'M', '2010-07-18', 'HR', 'Boston', 90000),
(110, 'David', 34, 'M', '2009-08-25', 'Product', 'Miami', 75000),
(111, 'Rose', 28, 'F', '2011-02-27', 'Tech', 'Chicago', 60000),
(112, 'Sophia', 33, 'F', '2013-09-21', 'HR', 'Houston', 65000),
(113, 'Amelia', 30, 'F', '2018-10-15', 'Finance', 'Austin', 55000),
(114, 'Robert', 40, 'M', '2015-12-18', 'Sales', 'Detroit', 95000),
(115, 'William', 36, 'M', '2016-04-20', 'IT', 'Chicago', 83000),
(116, 'John', 32, 'M', '2004-08-09', 'Marketing', 'Miami', 67000),
(117, 'Bella', 29, 'F', '2002-06-11', 'Tech', 'Detroit', 72000),
(118, 'Maya', 25, 'F', '2018-10-15', 'IT', 'Houston', 48000),
(119, 'Alice', 37, 'F', '2019-05-28', 'Product', 'Seattle', 76000),
(120, 'Joseph', 45, 'M', '2016-11-23', 'Sales', 'Chicago', 115000);

select * from employees1;

# Select Salary less than average Salary of the employees
select emp_name,Salary from employees1 
where Salary < (Select avg(Salary) from employees1);

#EXAMPLES
# Select Salary greater than average Salary of the employees
SELECT emp_name,Salary from employees1
where Salary > (Select avg(Salary) from employees1);

select * from employees1;
# Find the salary of the employeee greater than johns salary
SELECT emp_name, Salary from employees1 where Salary > 
(Select Salary from employees1 where emp_name = 'John');


#Subquerries using INSERT
create table products 
(prod_id int, item varchar(50), sell_price float, product_type varchar(50));

insert into products
values(101, 'Jewellery', 1800,'Luxury'),
(102,'T-Shirt',100,'Non-Luxury'),
(103,'Laptop',1300,'Luxury'),
(104,'Table',400,'Non-Luxury');

select * from products;

create table orders
(order_id int, product_sold varchar(50),selling_price float);
select * from orders;

#INSERT Function
insert into orders(
Select prod_id, item, sell_price
from products where prod_id in
(Select prod_id from products where sell_price > 1000));

#Subqueries using UPDATE
create table employee_b(Emp_Id int primary key, Emp_Name varchar(25),
Age int, Gender char(1), Doj date, Dept varchar(20), City varchar(20),
Salary float);

insert into employee_b(select * from employees);
select * from employee_b;

update employee_b
set salary = salary * 0.35
where emp_id in (select emp_id from employees where age >= 27);

select * from employee_b;

#Subquery using DELETE Statement

delete from employees
where emp_id in (select emp_id from employee_b where age <=32);

select * from employees;


create table emp(
    Emp_Id INT PRIMARY KEY,
    Emp_Name VARCHAR(50),
    Age INT,
    Gender CHAR(1),
    Doj DATE,
    Dept VARCHAR(50),
    City VARCHAR(50),
    Salary INT
);

INSERT INTO emp (Emp_Id, Emp_Name, Age, Gender, Doj, Dept, City, Salary) VALUES
(101, 'Jimmy', 35, 'M', '2005-05-30', 'Sales', 'Chicago', 70000),
(102, 'Shane', 30, 'M', '1999-06-25', 'Marketing', 'Seattle', 55000),
(103, 'Marry', 28, 'F', '2009-03-10', 'Product', 'Boston', 62000),
(104, 'Dwayne', 37, 'M', '2011-07-12', 'Tech', 'Austin', 57000),
(105, 'Sara', 32, 'F', '2017-10-27', 'Sales', 'New York', 72000),
(106, 'Ammy', 35, 'F', '2014-12-20', 'IT', 'Seattle', 80000),
(107, 'Jack', 40, 'M', '2012-07-14', 'Finance', 'Houston', 100000),
(108, 'Angela', 36, 'F', '2007-02-04', 'Tech', 'New York', 110000),
(109, 'Marcus', 25, 'M', '2010-07-18', 'HR', 'Boston', 90000),
(110, 'David', 34, 'M', '2009-08-25', 'Product', 'Miami', 75000),
(111, 'Rose', 28, 'F', '2011-02-27', 'Tech', 'Chicago', 60000),
(112, 'Sophia', 33, 'F', '2013-09-21', 'HR', 'Houston', 65000),
(113, 'Amelia', 30, 'F', '2018-10-15', 'Finance', 'Austin', 55000),
(114, 'Robert', 40, 'M', '2015-12-18', 'Sales', 'Detroit', 95000),
(115, 'William', 36, 'M', '2016-04-20', 'IT', 'Chicago', 83000),
(116, 'John', 32, 'M', '2004-08-09', 'Marketing', 'Miami', 67000),
(117, 'Bella', 29, 'F', '2002-06-11', 'Tech', 'Detroit', 72000),
(118, 'Maya', 25, 'F', '2018-10-15', 'IT', 'Houston', 48000),
(119, 'Alice', 37, 'F', '2019-05-28', 'Product', 'Seattle', 76000),
(120, 'Joseph', 45, 'M', '2016-11-23', 'Sales', 'Chicago', 115000);

set SQL_SAFE_UPDATES = 0;
delete from emp
where age in (select age from (select age from emp where age <=32) as temp) ;
set SQL_SAFE_UPDATES = 1;
SELECT * FROM EMP;


#Subqueries with two different table
show databases;
use classicmodels;
show tables;

# want to know the product code, product name, and msrp of the products whose price 
#of each product is less than 100

select productcode,productname,msrp from products
where productcode in (select productcode from orderdetails
where priceeach < 100);