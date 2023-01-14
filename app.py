
import sqlite3
from flask import Flask, render_template, url_for, flash, redirect, request

app = Flask(__name__)
app.config['SECRET_KEY']="dragon"

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    for user in users:
        print(user['email'])
    conn.close()
    return render_template('index.html', users=users)

@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'GET':
        return render_template('register.html')
    # TODO: Aarav, you need to add the code to insert the user into the database.
    # TODO: Aarav, you need to add the code to redirect to the index page.
    return render_template('register.html')

