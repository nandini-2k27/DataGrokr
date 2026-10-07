USE analytics_db;


-- ==========================================
-- DATE DATA
-- ==========================================

INSERT INTO dim_date
(date_id, full_date, month, month_name, year)
VALUES
(1, '2026-01-10', 1, 'January', 2026),
(2, '2026-01-15', 1, 'January', 2026),
(3, '2026-02-05', 2, 'February', 2026),
(4, '2026-02-18', 2, 'February', 2026),
(5, '2026-03-08', 3, 'March', 2026),
(6, '2026-03-20', 3, 'March', 2026),
(7, '2026-04-05', 4, 'April', 2026),
(8, '2026-04-22', 4, 'April', 2026),
(9, '2026-05-10', 5, 'May', 2026),
(10, '2026-05-25', 5, 'May', 2026);


-- ==========================================
-- CUSTOMER DATA
-- ==========================================

INSERT INTO dim_customer
(customer_id, customer_name, city, customer_segment)
VALUES
(1, 'Nandini', 'Bangalore', 'Premium'),
(2, 'Rahul', 'Delhi', 'Regular'),
(3, 'Priya', 'Mumbai', 'Premium'),
(4, 'Aman', 'Pune', 'Regular'),
(5, 'Sneha', 'Chennai', 'Premium');


-- ==========================================
-- PRODUCT DATA
-- ==========================================

INSERT INTO dim_product
(product_id, product_name, category, price)
VALUES
(1, 'Laptop', 'Electronics', 65000),
(2, 'Headphones', 'Electronics', 2500),
(3, 'Backpack', 'Accessories', 1800),
(4, 'Smartphone', 'Electronics', 35000),
(5, 'Keyboard', 'Electronics', 3000),
(6, 'Mouse', 'Electronics', 1500);


-- ==========================================
-- STORE DATA
-- ==========================================

INSERT INTO dim_store
(store_id, store_name, city)
VALUES
(1, 'Bangalore Central', 'Bangalore'),
(2, 'Delhi Central', 'Delhi'),
(3, 'Mumbai Central', 'Mumbai');


-- ==========================================
-- FACT SALES DATA
-- ==========================================

INSERT INTO fact_sales
(sale_id, date_id, customer_id, product_id, store_id,
 quantity, sales_amount, discount, profit)
VALUES

(101, 1, 1, 1, 1, 1, 65000, 2000, 8000),
(102, 2, 2, 2, 2, 2, 5000, 500, 1500),

(103, 3, 3, 4, 3, 1, 35000, 1500, 6000),
(104, 4, 4, 3, 2, 3, 5400, 300, 1800),

(105, 5, 1, 5, 1, 2, 6000, 400, 2000),
(106, 6, 5, 6, 3, 4, 6000, 200, 2200),

(107, 7, 2, 4, 2, 1, 35000, 1000, 6000),
(108, 8, 3, 1, 3, 1, 65000, 3000, 8500),

(109, 9, 4, 2, 2, 3, 7500, 500, 2500),
(110, 10, 5, 5, 3, 2, 6000, 300, 2100);