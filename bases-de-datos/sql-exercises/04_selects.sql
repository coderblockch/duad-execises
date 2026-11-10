-- 1. Get all products
SELECT * FROM products;

-- 2. Get all products with price greater than 50000
SELECT * FROM products WHERE price > 50000;

-- 3. Get all purchases of the same product by id
SELECT * FROM products_per_invoice WHERE product_id = 2;

-- 4. Get all purchases grouped by product, showing the total purchased
SELECT product_id, 
SUM(quantity) AS total_quantity,
SUM(total_amount) AS total_amount
FROM products_per_invoice
GROUP BY product_id;

-- 5. Get all invoices from the same buyer
SELECT * FROM invoices WHERE buyer_email = 'ana@mail.com';

-- 6. Get all invoices ordered by total amount in descending order
SELECT * FROM invoices ORDER BY total_amount DESC;

-- 7. Get a single invoice by invoice number
SELECT * FROM invoices WHERE invoice_number = 'INV-002';



