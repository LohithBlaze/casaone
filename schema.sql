CREATE TABLE rating (
    productId TEXT NOT NULL,
    userId TEXT NOT NULL,
    rating INTEGER
);

CREATE TABLE user (
    userId TEXT PRIMARY KEY,
    email TEXT NOT NULL,
    productId TEXT
);

CREATE TABLE product (
    productId TEXT PRIMARY KEY,
    price TEXT NOT NULL
);

