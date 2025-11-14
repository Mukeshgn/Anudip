show databases;
use classicmodels;
select * from customers;
#Views in SQL

create view cust_details as
select customerName, phone, city
from customers;

#To view 
select * from cust_details;

# Create view using JOINS
Select * from products;
Select * from productlines;


CREATE VIEW product_description 
AS
SELECT productName, quantityinstock,msrp,textdescription
FROM products AS p inner join productlines as pl
on p.productline = pl.productline;

select * from product_description;

#RENAME description
rename table product_description to vehicle_description;

#Display views
show full tables
where table_type = 'VIEW';

#Delete a view
Drop view cust_details;


