
import sqlite3
from flask import Flask, render_template, url_for, flash, redirect, request, session
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from dotenv import load_dotenv
from os import getenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY']="dragon"

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    print('here')
    print(session)
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    for user in users:
        print(user['email'])
    conn.close()
    return render_template('index.html', users=users, name=[session['name']] if 'name' in session else None)

@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'GET':
        return render_template('register.html')
    # TODO: Aarav, you need to add the code to insert the user into the database.
    print(request.form["email"])
    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute("INSERT INTO users (email, person, age, phone, country, cohort, addr) VALUES (?,?, ?, ?, ?, ?, ?)",
                (request.form["email"], request.form["name"],request.form["age"] ,request.form["phone"] ,
                'America', '0',request.form["address"])
                )

    connection.commit()
    connection.close()
    flash("You have successfully registered")
    # TODO: Aarav, you need to add the code to redirect to the index page.
    return redirect('/')

@app.route('/login', methods=('GET', 'POST'))
def login():
    print('login route')
    if request.method == 'GET':
        return render_template('login.html')
    connection = get_db_connection()

    cur = connection.cursor()
    user = cur.execute('SELECT * FROM users where email = ?', (request.form['email'],)).fetchone()
    if user:
        for item in user:
            print(f"{item}")
        session['logged_in'] = True
        session['name'] = user['person']
        print(session)

        account_sid = getenv('account_sid')
        auth_token = getenv('auth_token')
        demo_num = getenv('demo_num')
        from_num = getenv('from_num')

        client = Client(account_sid, auth_token)

        # As we are using Twilio's free tier, we can only send text messages to verified numbers.
        # This means that we must verify each users phone # with twilio. Because of this, we will use a
        # hardcoded phone number in the demo. In practice, you would use the user's phone number, which
        # can be accessed via the request.form object

        try:
            message = client.messages.create(
                to=demo_num, 
                from_=from_num,
                body="Please enter the following code to continue logging into the demo site: 241353")
        except TwilioRestException as err:
            print("Twilio authentication has failed")
            print(err)
        flash('You have successfully logged in')

    return redirect(url_for('index'))