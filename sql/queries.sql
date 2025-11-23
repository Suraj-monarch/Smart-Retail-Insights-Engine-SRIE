-- Total Revenue
SELECT SUM(Quantity * Price) AS TotalRevenue FROM sales_data;

-- Revenue by City
SELECT City, SUM(Quantity * Price) AS Revenue
FROM sales_data
GROUP BY City
ORDER BY Revenue DESC;

-- Top Customers
SELECT CustomerName, SUM(Quantity * Price) AS TotalSpent
FROM sales_data
GROUP BY CustomerName
ORDER BY TotalSpent DESC
LIMIT 5;

-- Product Sales Count
SELECT Product, COUNT(*) AS TotalOrders
FROM sales_data
GROUP BY Product;

-- Order Status Distribution
SELECT Status, COUNT(*) 
FROM sales_data
GROUP BY Status;

-- Monthly Trend
SELECT MONTH(OrderDate) AS MonthNum,
       SUM(Quantity * Price) AS Revenue
FROM sales_data
GROUP BY MonthNum
ORDER BY MonthNum;
