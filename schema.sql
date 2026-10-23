CREATE TABLE IF NOT EXISTS products (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  price NUMERIC(8,2) NOT NULL
);

INSERT INTO products (name, price) VALUES
  ('Notebook', 4.50),
  ('Pen Set', 3.25),
  ('Desk Lamp', 18.99),
  ('Backpack', 32.00);
