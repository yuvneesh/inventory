import sqlite3
import graphviz

# Replace 'your_database.db' with the path to your SQLite database
database_path = 'site.db'

# Connect to the SQLite database
conn = sqlite3.connect(database_path)
cursor = conn.cursor()

# Query to extract table information
tables_query = "SELECT name FROM sqlite_master WHERE type='table';"
cursor.execute(tables_query)
tables = cursor.fetchall()

# Setup Graphviz diagram
dot = graphviz.Digraph(comment='Database Schema', format='png')

for table in tables:
    table_name = table[0]
    dot.node(table_name, table_name)
    
    # Query to find foreign keys for the current table
    fk_query = f"PRAGMA foreign_key_list({table_name});"
    cursor.execute(fk_query)
    fks = cursor.fetchall()
    
    for fk in fks:
        # Here, fk[2] is the table that the current table references, 
        # and fk[3] and fk[4] are the referencing and referenced columns respectively.
        dot.edge(table_name, fk[2], label=f"{fk[3]} -> {fk[4]}")

# Save the diagram to a file
filename = dot.render(filename='database_schema')
print(f"Diagram saved as: {filename}")
