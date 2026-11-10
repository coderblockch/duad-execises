PRAGMA foreign_keys = ON;

INSERT INTO products (code, name, price, entry_date, brand, stock) VALUES
    ('P001', 'Laptop', 450000, '2026-01-15', 'Lenovo', 10),
    ('P002', 'Mouse', 8500, '2026-02-01', 'Logitech', 50),
    ('P003', 'Monitor', 120000, '2026-02-10', 'Samsung', 15),
    ('P004', 'Keyboard', 25000, '2026-03-05', 'Redragon', 30),
    ('P005', 'Headphones', 65000, '2026-03-20', 'Sony', 20);

INSERT INTO invoices (invoice_number, purchase_date, buyer_email, total_amount) VALUES
    ('INV-001', '2026-04-01', 'ana@mail.com', 467000),
    ('INV-002', '2026-04-03', 'luis@mail.com', 120000),
    ('INV-003', '2026-04-05', 'ana@mail.com', 90000);

INSERT INTO products_per_invoice (invoice_id, product_id, quantity, total_amount) VALUES
    (1, 1, 1, 450000),
    (1, 2, 2, 17000),
    (2, 3, 1, 120000),
    (3, 4, 1, 25000),
    (3, 5, 1, 65000);