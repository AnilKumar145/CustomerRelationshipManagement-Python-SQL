import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('crm_system.db')
cursor = conn.cursor()

# Sample Query: Total sales by customer
cursor.execute('''
    SELECT c.name, SUM(s.quantity * p.price) AS total_spent
    FROM sales s
    JOIN customers c ON s.customer_id = c.customer_id
    JOIN products p ON s.product_id = p.product_id
    GROUP BY c.customer_id;
''')
results = cursor.fetchall()

# Display results
print("Total Sales by Customer:")
for row in results:
    print(f"Customer: {row[0]}, Total Spent: {row[1]}")

# Sample Query: Open support tickets
cursor.execute('''
    SELECT c.name, t.issue
    FROM support_tickets t
    JOIN customers c ON t.customer_id = c.customer_id
    WHERE t.status = 'Open';
''')
tickets = cursor.fetchall()

# Display open tickets
print("\nOpen Support Tickets:")
for ticket in tickets:
    print(f"Customer: {ticket[0]}, Issue: {ticket[1]}")

# Close connection
cursor.close()
conn.close()
