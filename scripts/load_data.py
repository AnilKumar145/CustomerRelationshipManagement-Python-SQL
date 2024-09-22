import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('crm_system.db')
cursor = conn.cursor()

# Load CSV data into DataFrames
customers_df = pd.read_csv('data/customers.csv')
sales_df = pd.read_csv('data/sales.csv')
products_df = pd.read_csv('data/products.csv')
tickets_df = pd.read_csv('data/support_tickets.csv')

# Insert customers data into SQLite
for index, row in customers_df.iterrows():
    cursor.execute(
        "INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)",
        (row['name'], row['email'], row['phone'])
    )

# Insert sales data into SQLite
for index, row in sales_df.iterrows():
    cursor.execute(
        "INSERT INTO sales (customer_id, product_id, quantity, sale_date) VALUES (?, ?, ?, ?)",
        (row['customer_id'], row['product_id'], row['quantity'], row['sale_date'])
    )

# Insert products data into SQLite
for index, row in products_df.iterrows():
    cursor.execute(
        "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)",
        (row['name'], row['price'], row['stock'])
    )

# Insert support tickets data into SQLite
for index, row in tickets_df.iterrows():
    cursor.execute(
        "INSERT INTO support_tickets (customer_id, issue, status) VALUES (?, ?, ?)",
        (row['customer_id'], row['issue'], row['status'])
    )

# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()

print("Data loaded successfully.")
