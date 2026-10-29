CREATE TABLE `products`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `code` VARCHAR(50) NOT NULL,
    `name` VARCHAR(100) NOT NULL,
    `price` DECIMAL(10, 2) NOT NULL,
    `entry_date` DATE NOT NULL,
    `brand` VARCHAR(100) NOT NULL,
    `stock` INT NOT NULL
);
CREATE TABLE `products_per_invoice`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `invoice_id` BIGINT NOT NULL,
    `product_id` BIGINT NOT NULL,
    `quantity` INT NOT NULL,
    `total_amount` DECIMAL(10, 2) NOT NULL
);
CREATE TABLE `invoices`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `invoice_number` VARCHAR(50) NOT NULL,
    `purchase_date` DATE NOT NULL,
    `buyer_email` VARCHAR(100) NOT NULL,
    `total_amount` DECIMAL(10, 2) NOT NULL
);
CREATE TABLE `shopping_cart`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `buyer_email` VARCHAR(100) NOT NULL
);
CREATE TABLE `cart_products`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `cart_id` BIGINT NOT NULL,
    `product_id` BIGINT NOT NULL,
    `quantity` INT NOT NULL
);
ALTER TABLE
    `products_per_invoice` ADD CONSTRAINT `products_per_invoice_invoice_id_foreign` FOREIGN KEY(`invoice_id`) REFERENCES `invoices`(`id`);
ALTER TABLE
    `products_per_invoice` ADD CONSTRAINT `products_per_invoice_product_id_foreign` FOREIGN KEY(`product_id`) REFERENCES `products`(`id`);
ALTER TABLE
    `cart_products` ADD CONSTRAINT `cart_products_cart_id_foreign` FOREIGN KEY(`cart_id`) REFERENCES `shopping_cart`(`id`);
ALTER TABLE
    `cart_products` ADD CONSTRAINT `cart_products_product_id_foreign` FOREIGN KEY(`product_id`) REFERENCES `products`(`id`);