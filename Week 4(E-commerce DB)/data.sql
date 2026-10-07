USE ecommerce_db;

INSERT INTO customers (customer_id, customer_name, email) VALUES
(1, 'Nandini', 'nandini@example.com'),
(2, 'Rahul', 'rahul@example.com'),
(3, 'Priya', 'priya@example.com'),
(4, 'Aman', 'aman@example.com'),
(5, 'Sneha', 'sneha@example.com');

INSERT INTO products (product_id, product_name, category, price) VALUES
(1, 'Laptop', 'Electronics', 65000.00),
(2, 'Headphones', 'Electronics', 2500.00),
(3, 'Backpack', 'Accessories', 1800.00),
(4, 'Smartphone', 'Electronics', 35000.00),
(5, 'Keyboard', 'Electronics', 3000.00),
(6, 'Mouse', 'Electronics', 1500.00),
(7, 'Running Shoes', 'Footwear', 4500.00),
(8, 'Watch', 'Accessories', 5000.00);

INSERT INTO orders (order_id, customer_id, order_date) VALUES
(101, 1, '2026-01-15'),
(102, 2, '2026-01-18'),
(103, 3, '2026-02-05'),
(104, 1, '2026-02-20'),
(105, 4, '2026-03-10'),
(106, 5, '2026-03-15'),
(107, 2, '2026-04-02'),
(108, 3, '2026-04-20'),
(109, 1, '2026-05-05'),
(110, 5, '2026-05-18');

INSERT INTO order_items
(order_item_id, order_id, product_id, quantity) VALUES
(1, 101, 1, 1),
(2, 101, 2, 2),
(3, 102, 4, 1),
(4, 102, 6, 2),
(5, 103, 3, 2),
(6, 103, 7, 1),
(7, 104, 5, 2),
(8, 104, 2, 1),
(9, 105, 8, 1),
(10, 105, 3, 2),
(11, 106, 7, 2),
(12, 106, 6, 1),
(13, 107, 4, 1),
(14, 107, 2, 2),
(15, 108, 1, 1),
(16, 108, 5, 1),
(17, 109, 8, 2),
(18, 109, 3, 1),
(19, 110, 4, 1),
(20, 110, 6, 3);