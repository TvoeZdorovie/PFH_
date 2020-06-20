from flask_wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class RegForm(Form):
    login = TextField('login', validators = [Required()])
    password = TextField('passwd' , validators = [Required()])
    name = TextField('name' , validators = [Required()])
    
    remember_me = BooleanField('remember_me', default = False)

class LoginForm(Form):
    login = TextField('login', validators = [Required()])
    password = TextField('passwd' , validators = [Required()])
    
    remember_me = BooleanField('remember_me', default = False)