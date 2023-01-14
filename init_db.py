"""Initialize Database"""
import sqlite3
import os

# Connect to local sqlite database file. Creates file is does not exist.
connection = sqlite3.connect('database.db')

# Run schema.sql script, this creates the table to be used
with open("schema.sql", encoding="utf-8") as f:
    connection.executescript(f.read())

# Create Cursor Object, Allows you to interact with DB.
cur = connection.cursor()

# Create two sample people, just for fun.
cur.execute("INSERT INTO users (email, person, age, phone, country, cohort, addr) VALUES (?,?, ?, ?, ?, ?, ?)",
            ('melwaninate@gmail.com', 'Nate Melwani', 21, '7148512888', 'country', '1', '900 universary ave')
            )

connection.commit()
connection.close()
