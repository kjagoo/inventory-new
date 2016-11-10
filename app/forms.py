from flask_wtf import Form

from wtforms import TextField, BooleanField, TextField, TextAreaField, SubmitField, validators, ValidationError, PasswordField
from wtforms.validators import Required

class ExampleForm(Form):
    dt = DateField('DatePicker', format='%Y-%m-%d')
    da = DateField('DatePicker', format='%Y-%m-%d')

class Assets(Form):
  name = TextField("name",  [validators.Required("Please enter your first name.")])
  serial = TextField("serial",  [validators.Required("Please enter your last name.")])
  a_serial = TextField("a_serial",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  description = TextField('description', [validators.Required("Please enter a password.")])
  date_bought = TextField('date_bought', [validators.Required("Please enter a password.")])
 
  submit = SubmitField("Create account")
 
  def __init__(self, name, serial,andela_serial,date_bought,description):
    Form.__init__(self, name, serial,andela_serial,date_bought,description)
 
  def validate(self):
    if not Form.validate(self):
      return "error validation"
     
    
class Staff(Form):
  f_name = TextField("f_name",  [validators.Required("Please enter your first name.")])
  s_name = TextField("s_name",  [validators.Required("Please enter your last name.")])
  username = TextField("username",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  level = TextField('level', [validators.Required("select the correct value.")])
  email = TextField('email', [validators.Required("Please enter a password.")])
 
  submit = SubmitField("Create account")
 
  def __init__(self, f_name, s_name,username,level,email):
    Form.__init__(self, f_name, s_name,username,level,email)
 
  def validate(self):
    if not Form.validate(self):
      return "error validation"

class Transactions(Form):
  staff_id = TextField("staff_id",  [validators.Required("Please enter your first name.")])
  asset_id = TextField("asset_id",  [validators.Required("Please enter your last name.")])
  admin_id = TextField("admin_id",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  date_borrowed = TextField('date_borrowed', [validators.Required("select the correct value.")])
  date_returned = TextField('date_returned', [validators.Required("Please enter a password.")])
  #status = TextField('status', [validators.Required("select the correct value.")])
  comment = TextField('comment', [validators.Required("Please enter a password.")])
 
  submit = SubmitField("Create account")
 
  def __init__(self, staff_id, asset_id,admin_id,date_borrowed,date_returned,comment):
    Form.__init__(self, staff_id, asset_id,admin_id,date_borrowed,date_returned,comment)
 
  def validate(self):
    if not Form.validate(self):
      return "error validation"
