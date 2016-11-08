from app import app
from flask import url_for
from flask import Flask, flash, redirect, render_template, request, session, abort
import MySQLdb

''' connect to database''' 
db = MySQLdb.connect(host="localhost", user="ODBC", passwd="", db="invent_management")
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
cur = db.cursor()


@app.route('/')
@app.route('/index')

def index():

    
    return render_template('index.html', title='Home')

''' log in function , check if user is on staff table'''

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username_form  = request.form['username']
        password_form  = request.form['password']

        cur.execute("SELECT COUNT(1) FROM tbl_staff WHERE username = %s;", [username_form]) # CHECKS IF USERNAME EXSIST
        if cur.fetchone()[0]:
            cur.execute("SELECT password FROM tbl_staff WHERE password = %s;", [username_form]) # FETCH THE HASHED PASSWORD
            for row in cur.fetchall():
                if password_form == row[0]:
                    session['username'] = request.form['username']
                    return redirect(url_for('index'))
                else:
                    error = "Invalid Credential"
        
    return render_template('login.html', error=error)

@app.route('/add_asset', methods=['GET', 'POST'])
def add_asset():
    error = None
    if request.method == 'POST':
        name_form  = request.form['name']
        description_form  = request.form['description']
        serial_form  = request.form['serial']
        a_serial_form  = request.form['a_serial']
        date_bought_form  = request.form['date_bought']

        return [name_form, serial_form, a_serial_form, date_bought_form]

        cur.execute("""insert into tbl_assets (name,serial,andela_serial,date_bought,description)
values (%s, %s, %s, %s, %s)""", [name_form, serial_form, a_serial_form, date_bought_form, description_form])
        db.commit()
        
        return "Successfully Added"
    else:
        error = "Invalid Credential"
        
    return render_template('add_asset.html', error=error)

