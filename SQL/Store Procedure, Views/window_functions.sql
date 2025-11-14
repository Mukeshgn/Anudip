show databases;
use sql_intro;
show tables;
Select * from employees;

select emp_name, age,dept,
SUM(Salary) over(partition by Dept) AS total_salary
from employees;

select Dept,SUM(Salary) from employees group by Dept;

#Row number
SELECT row_number() OVER(order by Salary) AS Row_num, 
emp_name,Salary from employees Order by Salary;

#truncate table demo;
CREATE TABLE Demo (st_id int, st_name varchar(20));
insert into demo
values(101,'Shane'),
(102,'Bradley'),
(103,'Herath'),
(103,'Herath'),
(104,'Nathan'),
(105,'Kevin'),
(105,'Kevin');
select * from demo;


SELECT st_id, st_name, row_number() over
(partition by st_id,st_name order by St_id) as row_num
from demo;

#RANK function

create table demo1(var_a int);
insert into demo1
values(101),(102),(103),(103),(104),(105),(106),(106),(107);

select var_a, rank() over(order by var_a) as test_rank
from demo1;

#FIREST VALUE()
Select emp_name, dept, salary, first_value(emp_name)
Over(partition by dept order by Salary desc) as highest_salary 
from employees;


#ROW_NUMBER (Numbering employees by rank inside each department.)
SELECT 
    emp_name,
    dept,
    salary,
    ROW_NUMBER() OVER (PARTITION BY salary ORDER BY salary DESC) AS row_num
FROM employees;


#RANK() - ranking salaries where ties cause skipped ranks (1, 2, 2, 4).
SELECT 
    emp_name,
    dept,
    salary,
    RANK() OVER (PARTITION By salary ORDER BY salary DESC) AS rank_gap
FROM employees;

#DENSE_RANK() - ranking without gaps (1, 2, 2, 3).
SELECT 
    emp_name,
    dept,
    salary,
    DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS denserank
FROM employees;


# All Window keys

CREATE TABLE sales1 (
    emp_id INT,
    emp_name VARCHAR(50),
    region VARCHAR(20),
    month VARCHAR(10),
    sales_amount INT
);

INSERT INTO sales1 (emp_id, emp_name, region, month, sales_amount)
VALUES
(1, 'Ramesh', 'South', 'Jan', 50000),
(2, 'Priya', 'South', 'Jan', 45000),
(3, 'Kiran', 'South', 'Feb', 52000),
(4, 'Arjun', 'North', 'Jan', 70000),
(5, 'Sneha', 'North', 'Jan', 68000),
(6, 'Rahul', 'North', 'Feb', 75000),
(7, 'Anjali', 'East', 'Jan', 40000),
(8, 'Dev', 'East', 'Feb', 42000),
(9, 'Neha', 'West', 'Jan', 60000),
(10, 'Vivek', 'West', 'Feb', 63000);

SELECT 
    emp_name,
    region,
    month,
    sales_amount,

    -- 1️⃣ Ranking and Numbering
    ROW_NUMBER() OVER (PARTITION BY region ORDER BY sales_amount DESC) AS row_num,
    RANK() OVER (PARTITION BY region ORDER BY sales_amount DESC) AS rank_gap,
    DENSE_RANK() OVER (PARTITION BY region ORDER BY sales_amount DESC) AS denserank,

    -- 2️⃣ Regional aggregates
    SUM(sales_amount) OVER (PARTITION BY region) AS total_sales_region,
    AVG(sales_amount) OVER (PARTITION BY region) AS avg_sales_region,
    MAX(sales_amount) OVER (PARTITION BY region) AS max_sales_region,
    MIN(sales_amount) OVER (PARTITION BY region) AS min_sales_region,

    -- 3️⃣ Running total & comparison
    SUM(sales_amount) OVER (PARTITION BY region ORDER BY month) AS running_sales,
    LAG(sales_amount) OVER (PARTITION BY region ORDER BY month) AS prev_month_sales,
    LEAD(sales_amount) OVER (PARTITION BY region ORDER BY month) AS next_month_sales

FROM sales1;
