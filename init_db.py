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
            ('melwaninate@gmail.com', 'Nate Melwani', 21, '7148512888', 'country', '0', '900 universary ave')
            )

cur.execute("INSERT INTO cohorts (leader, leaderpicurl, descrip, place) VALUES (?,?,?,?)",
            ('Chloe Au', 'https://media.licdn.com/dms/image/D5603AQHv62HMBlQ2sA/profile-displayphoto-shrink_100_100/0/1646702660645?e=1679529600&v=beta&t=EPYRd_O1mz8Lk54bBW3jKYYtrMFg_6IcZyzlnQQ0TLk', " Chloe is a strong advocate for the use of technology to improve the lives of others. She has a background in software engineering and is currently pursuing a Bachler's degree in Data Science.", 'Beijing, CN')
            )

cur.execute("INSERT INTO cohorts (leader, leaderpicurl, descrip, place) VALUES (?,?,?,?)",
            ('Pikachu',
            'https://i.pinimg.com/originals/bf/95/34/bf953419d76bf747cba69b55e6e03957.png',
            'PIkachu from Pokemon',
            'Kanto, Japan')
            )

connection.commit()
connection.close()
