CREATE DATABASE RetailDB;
USE RetailDB;

CREATE TABLE sales_data (
    OrderID INT,
    CustomerName VARCHAR(100),
    City VARCHAR(100),
    Product VARCHAR(50),
    Quantity INT,
    Price INT,
    OrderDate DATE,
    Status VARCHAR(50)
);
