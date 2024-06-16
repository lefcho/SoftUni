CREATE TABLE products(
	product_name varchar(100)
);

INSERT INTO 
	products(product_name)
VALUES
	('Broccoli'),
	('Shampoo'),
	('Toothpaste'),
	('Candy');
    
ALTER TABLE
	products
ADD column
	"id" SERIAL PRIMARY KEY;
