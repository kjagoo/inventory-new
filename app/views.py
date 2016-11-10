from app import app
from flask import url_for
from flask import Flask, flash, redirect, render_template, request, session, abort
from flask import Flask,jsonify,abort, make_response
from sqlalchemy import *
from db import Add_asset, Add_staff, Issue_asset,UserRights
from db import session as sess
from flask_wtf import Form
from wtforms.fields.html5 import DateField
from datetime import date
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'



class ExampleForm(Form):
    dt = DateField('DatePicker', format='%Y-%m-%d')
    da = DateField('DatePicker', format='%Y-%m-%d')


'''----------------------  log in method  -----------------------------------------'''
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    ''' log in function , check if user is on staff table, if True login else go to log in page'''
    error = None
    session['logged_in'] = False
    if request.method == 'POST':
        username_form  = request.form['username']
        password_form  = request.form['password']

        all_records = sess.query(Add_staff).filter_by(username=username_form).first()
        return all_records.department_id
        if all_records.department_id==1 and all_records.right_id==2:
            all_records.right_id=2
        elif  all_records.department_id==1 and all_records.right_id!=2:
            all_records.right_id=2
    
            
        if password_form == all_records.password:
            
            session['username'] = request.form['username']
            session['rights'] = all_records.right_id
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            error = "Invalid Credentials"
        
        
    return render_template('login.html', error=error)



'''---------------------------   index page----------------------------------------------'''
@app.route('/index')
def index():
    if session['logged_in'] == True:
        assets = sess.query(Add_asset).count()
        staff = sess.query(Add_staff).count()
        transactions = sess.query(Issue_asset).count()
        user=session['rights']
        return render_template('index.html', title='Home',user=user , assets=assets, staff=staff,transactions=transactions)
    else:
        return redirect(url_for('login'))
    return render_template('index.html', title='Home' ,user=user)


''' ----------------------------  add asset-----------------------------------------------'''
@app.route('/add_asset', methods=['GET', 'POST'])
def add_asset():
    #insert into tbl_assets in database
    error = None
    user=session['rights']
    form = ExampleForm()
    if form.validate_on_submit():
        return form.da.data.strftime('%Y-%m-%d')
    if request.method == 'POST':
        
        if request.form['add']:
            
            name_form  = request.form['name']
            description_form  = request.form['description']
            serial_form  = request.form['serial']
            a_serial_form  = request.form['a_serial']
            date_bought_form  = request.form['da']
            new_record = Add_asset(name_form, serial_form, a_serial_form, date_bought_form, description_form)
            sess.add(new_record)
            sess.commit()
             
            
            return render_template('add_asset.html',form=form,user=user)
        else:
            return render_template('add_asset.html', error=error,form=form,user=user)
    else:
        error = "Form Post not Received"
        
    return render_template('add_asset.html',error=error, form =form,user=user)



'''----------------------------------   view assets  ------------------------------------'''
@app.route('/view_assets', methods=['GET', 'POST'])
def view_assets():
    user=session['rights']

    all_records = sess.query(Add_asset).all()
    
    all_trans = sess.query(Issue_asset).all()
    return render_template('view_assets.html', all_records=all_records, all_trans=all_trans,user=user)
       


'''----------------------------------   view assets  ------------------------------------'''
@app.route('/available_assets', methods=['GET', 'POST'])
def available_assets():
    user=session['rights']

    all_records = sess.query(Add_asset).all()
    
    all_trans = sess.query(Issue_asset).filter_by(status='Issued out')
    return render_template('available_assets.html', all_records=all_records, all_trans=all_trans,user=user)

 

'''----------------------------------   issue assets ------------------------------------'''
@app.route('/issue_asset/<transaction_id>', methods=['GET','POST'])
def reclaim_asset(transaction_id):
    
    all_records = sess.query(Issue_asset).filter_by(transaction_id=transaction_id).first()
    user=session['rights']
    today = date.today()

    #return "ghghghg: "+ all_records.status
    all_records.status='Reclaimed'
    all_records.date_returned=today
    
    sess.add(all_records)
    sess.commit()
    return redirect(url_for('reclaimed'))




@app.route('/issue_asset', methods=['GET', 'POST'])
def issue_asset():
    error = None
    all_staff = sess.query(Add_staff).all()# get staff list
    all_assets = sess.query(Add_asset).all()# get assets lits
    user=session['rights']
   

    form = ExampleForm()
    if form.validate_on_submit():
        return form.dt.data.strftime('%Y-%m-%d')#init date format

    if request.method == 'POST':
        
        if request.form['add']:
            
            staff_id  = request.form['staff_id']
            asset_id  = request.form['asset_id']
            admin_id  = session['username']
            date_borrowed  = request.form['dt']
            date_return  = request.form['da']
            status  = "Issued Out"
            comment  = request.form['comment']
            
            
            
            new_transaction = Issue_asset(staff_id, asset_id,admin_id,date_borrowed,date_return,status,comment)
            sess.add(new_transaction)
            sess.commit()
             
            flash('successfully submitted')
            return render_template('issue_asset.html',form=form,all_staff=all_staff,all_assets=all_assets,user=user )
        else:
            return render_template('issue_asset.html', error=error,user=user,form=form ,all_staff=all_staff,all_assets=all_assets)
    else:
        error = "Form Post not Received"
    return render_template('issue_asset.html',form=form ,all_staff=all_staff,all_assets=all_assets,user=user)


'''----------------------------------   add staff ------------------------------------'''
@app.route('/add_staff', methods=['GET', 'POST'])
def add_staff():
    error = None
    all_rights =sess.query(UserRights).all()
    user=session['rights']
    if request.method == 'POST':
        
        if request.form['add']:
            
            f_name  = request.form['f_name']
            s_name  = request.form['s_name']
            username  = request.form['username']
            level  = request.form['level']
            email  = request.form['email']
            
            new_staff = Add_staff(f_name, s_name,username,level,email)
            sess.add(new_staff)
            sess.commit()
             
            
            return render_template('add_staff.html',all_rights=all_rights,user=user)
        else:
            return render_template('add_staff.html', all_rights=all_rights,error=error,user=user)
    else:
        error = "Form Post not Received"
    return render_template('add_staff.html', error=error, all_rights=all_rights,user=user)


''' --------------------------      view staff ------------------------------------------------ '''
@app.route('/view_staff', methods=['GET', 'POST'])
def view_staff():
    user=session['rights']
    all_records = sess.query(Add_staff).all()
    all_rights =sess.query(UserRights).all()
    return render_template('view_staff.html', all_records=all_records,all_rights=all_rights,user=user )



@app.route('/view_transactions', methods=['GET', 'POST'])
def view_transactions():
    all_records = sess.query(Issue_asset).all()
    user=session['rights']
    today = date.today()
    all_staff = sess.query(Add_staff).all()# get staff names
    all_assets = sess.query(Add_asset).all()# get asset name
    
    return render_template('view_transactions.html', today = today, user=user, all_records=all_records, all_staff=all_staff,all_assets=all_assets)



"""----------------------------------- Reclaimed transactions-------------------------------------- """
@app.route('/reclaimed', methods=['GET', 'POST'])
def reclaimed():
    all_records = sess.query(Issue_asset).filter_by(status='Reclaimed')
    user=session['rights']
    today = date.today()
    all_staff = sess.query(Add_staff).all()# get staff names
    all_assets = sess.query(Add_asset).all()# get asset name
    
    return render_template('reclaimed.html', today = today, user=user, all_records=all_records, all_staff=all_staff,all_assets=all_assets)
      

"""----------------------------------- Issued transactions-------------------------------------- """
@app.route('/issued', methods=['GET', 'POST'])
def issued():
    all_records = sess.query(Issue_asset).filter_by(status='Issued Out')
    user=session['rights']
    today = date.today()
    all_staff = sess.query(Add_staff).all()# get staff names
    all_assets = sess.query(Add_asset).all()# get asset name
    
    return render_template('issued.html', today = today, user=user, all_records=all_records, all_staff=all_staff,all_assets=all_assets)
    
