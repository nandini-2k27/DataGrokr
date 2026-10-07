# E-Commerce Database Analysis

A SQL-based e-commerce database project designed to analyze product sales, customer spending, order trends, and revenue.

The project uses a relational database containing customers, products, orders, and order items. SQL queries are used to extract meaningful business insights from the data.

## Project Objectives

The project focuses on answering key e-commerce business questions:

- Which products sell the most?
- Which customers spend the most?
- How do order volumes change over time?
- How does revenue change month by month?
- What are the top three best-selling products?

## Database Structure

The project contains four related tables:

```text
customers
    │
    │ customer_id
    ▼
orders
    │
    │ order_id
    ▼
order_items
    │
    │ product_id
    ▼
products
```

### Tables

#### 1. Customers

Stores customer information.

| Column        | Description                |
| ------------- | -------------------------- |
| customer_id   | Unique customer identifier |
| customer_name | Customer name              |
| email         | Customer email             |

#### 2. Products

Stores product information.

| Column       | Description               |
| ------------ | ------------------------- |
| product_id   | Unique product identifier |
| product_name | Name of the product       |
| category     | Product category          |
| price        | Product price             |

#### 3. Orders

Stores customer order information.

| Column      | Description                   |
| ----------- | ----------------------------- |
| order_id    | Unique order identifier       |
| customer_id | Customer who placed the order |
| order_date  | Date of the order             |

#### 4. Order Items

Stores the products included in each order.

| Column        | Description                  |
| ------------- | ---------------------------- |
| order_item_id | Unique order item identifier |
| order_id      | Related order                |
| product_id    | Purchased product            |
| quantity      | Quantity purchased           |

## Technologies Used

- MySQL
- SQL
- MySQL Workbench

## SQL Concepts Used

This project demonstrates:

- `CREATE DATABASE`
- `CREATE TABLE`
- Primary Keys
- Foreign Keys
- `INSERT`
- `SELECT`
- `JOIN`
- `GROUP BY`
- `ORDER BY`
- `SUM()`
- `COUNT()`
- `LIMIT`
- `DATE_FORMAT()`
- Aggregate functions
- Relational database design

## Analysis Queries

### 1. Top-Selling Products

Determines which products have the highest number of units sold.

```sql
SELECT
    p.product_name,
    SUM(oi.quantity) AS total_units_sold
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_units_sold DESC;
```

### 2. Customer Spending

Calculates the total amount spent by each customer.

```sql
SUM(p.price * oi.quantity)
```

Customers are ranked from highest to lowest spending.

### 3. Monthly Order Trends

Counts the number of orders placed each month using `DATE_FORMAT()` and `COUNT()`.

### 4. Monthly Revenue

Calculates the total revenue generated in each month.

```text
Revenue = Product Price × Quantity
```

### 5. Top 3 Products

Uses `ORDER BY` and `LIMIT 3` to identify the three best-selling products.

## Example Results

### Top Products

Based on the sample dataset:

| Product    | Units Sold |
| ---------- | ---------: |
| Mouse      |          6 |
| Headphones |          5 |
| Backpack   |          5 |

The Mouse is the highest-selling product in the sample dataset.

## How to Run

### 1. Create the database

Open `schema.sql` in MySQL Workbench and execute it.

### 2. Insert sample data

Open `data.sql` and execute it after creating the database and tables.

### 3. Run analysis queries

Open `queries.sql` and execute the queries individually or together.

## Project Structure

```text
Week 4(E-commerce DB)/
│
├── schema.sql
├── data.sql
├── queries.sql
└── README.md
```

## Learning Outcomes

This project provides practical experience with:

- Relational database design
- SQL joins
- Data aggregation
- Business-oriented SQL analysis
- Primary and foreign keys
- Grouping and sorting data
- Date-based analysis
- Writing analytical SQL queries

## Author

**Nandini Yadav**

This project was developed as part of the **DataGrokr Weekly Test - Week 4**.
