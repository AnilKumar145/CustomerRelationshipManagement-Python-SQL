import sqlite3 

conn = sqlite3.connect('crm_system.db')
cursor = conn.cursor()

# Create customers table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
''')

# Create products table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL,
        stock INTEGER
    );
''')

# Create sales table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        product_id INTEGER,
        quantity INTEGER,
        sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    );
''')

# Create support_tickets table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS support_tickets (
        ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        issue TEXT,
        status TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    );
''')


conn.commit()
cursor.close()
conn.close()

print("Database schema created successfully.")