PRAGMA foreign_keys = ON;
DROP TABLE IF EXISTS cart_products;
DROP TABLE IF EXISTS products_per_invoice;
DROP TABLE IF EXISTS shopping_cart;
DROP TABLE IF EXISTS invoices;
DROP TABLE IF EXISTS products;

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE CHECK (length(code) <= 50),
    name TEXT NOT NULL CHECK (length(name) <= 100),
    price REAL NOT NULL CHECK (price >= 0),
    entry_date TEXT NOT NULL,
    brand TEXT NOT NULL CHECK (length(brand) <= 100),
    stock INTEGER NOT NULL CHECK (stock >= 0)
);
CREATE TABLE invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_number TEXT NOT NULL UNIQUE CHECK (length(invoice_number) <= 50),
    purchase_date TEXT NOT NULL,
    buyer_email TEXT NOT NULL CHECK (length(buyer_email) <= 100),
    total_amount REAL NULL CHECK (total_amount >= 0)
);
CREATE TABLE shopping_cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    buyer_email TEXT NOT NULL CHECK (length(buyer_email) <= 100)
);
CREATE TABLE products_per_invoice (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    total_amount REAL NOT NULL CHECK (total_amount >= 0),
    FOREIGN KEY (invoice_id) REFERENCES invoices(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
CREATE TABLE cart_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    FOREIGN KEY (cart_id) REFERENCES shopping_cart(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
