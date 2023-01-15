
import sqlite3
from flask import Flask, render_template, url_for, flash, redirect, request, session
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from dotenv import load_dotenv
from os import getenv
import random

from util.ISO3166 import countrycodes
from util.provinces import provinceMap
from util.jobdata import jobdata

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

@app.route('/verify')
def verify():
    return render_template('verify.html')

@app.route('/phone',methods=('GET', 'POST'))
def phone():
    if request.method == 'GET':
        return redirect(url_for('verify'))
    if int(request.form['code']) == int(session['code']):
        session['logged_in'] = True
        return redirect(url_for('index'))
    return render_template('verify.html')

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
        #session['logged_in'] = True
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

        if 'code' not in session:
            session['code'] = random.randint(100000, 999999) # Let's pretend you didnt see this

        try:
            message = client.messages.create(
                to=demo_num, 
                from_=from_num,
                body=f"Please enter the following code to continue logging into the demo site: {session['code']}")
        except TwilioRestException as err:
            print("Twilio authentication has failed")
            print(err)
        flash('Please enter the code sent to your phone')
        return redirect(url_for('verify'))

    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/portal')
def portal():
    print(session)
    if not 'logged_in' in session:
        return redirect(url_for('index'))
    if 'country' not in session:
        return redirect(url_for('country'))
    if 'job' not in session:
        return redirect(url_for('job'))
    return render_template('portal.html', country=session['country'], province=session['province'])

@app.route('/job', methods=('GET', 'POST'))
def job():
    if request.method == 'GET':
        return render_template('job.html')
    session['job'] = request.form['job']
    return redirect(url_for('portal'))

@app.route('/country', methods=('GET', 'POST'))
def country():
    if request.method == 'GET':
        return render_template('country.html')
    session['country'] = countrycodes[request.form['country-code']] if request.form['country-code'] in countrycodes else request.form['country-code']
    session['province'] = provinceMap[request.form['province-code']] if request.form['province-code'] in provinceMap else request.form['province-code']
    return redirect(url_for('portal'))

@app.route('/cohorts', methods=('GET', 'POST'))
def cohorts():
    if request.method == 'GET':
        conn = get_db_connection()
        cohorts = conn.execute('SELECT * FROM cohorts').fetchall()
        return render_template('cohorts.html', cohorts=cohorts)
    #conn = get_db_connection()
   # cohort = conn.execute('SELECT * FROM cohorts where id = ?', (request.form['cohort'],)).fetchone()
    print('in this func')
    session['cohort'] = request.form['cohort_number']
    #session['cohort_name'] = cohort['leader']
    flash('You have successfully registered and joined a cohort!')
    return redirect(url_for('portal'))

@app.get('/viewCohort')
def viewCohort():
    conn = get_db_connection()
    cohort = conn.execute('SELECT * FROM cohorts where id = ?', (session['cohort'],)).fetchone()
    return render_template('viewCohort.html', cohort=cohort)