


from flask import render_template , flash, redirect , session , url_for, request , g
from flask_login import login_user, logout_user, current_user, login_required
from app import app , db , models
from .forms import LoginForm , RegForm
from .models import User, ROLE_USER, ROLE_ADMIN
from helper import check_email

@app.route('/')
@app.route('/index')
@login_required
def index():

    print(current_user.is_authenticated)
    user = { 'name': current_user.name }
    return render_template("index.html",
        title = 'Кабинет',
        user = user)

@app.route('/reg', methods = ['GET', 'POST'])
def reg():
    
    form = RegForm()
    if form.validate_on_submit():
        if not check_email(form.login.data):
            flash('Проверьте адрес электронной почты')
            return redirect(url_for('reg'))

        #flash('Привет ' + form.login.data )    
        u = models.User(email=form.login.data , passwd=form.password.data,name=form.name.data, role=models.ROLE_USER)
        u.hash_password()
        try:
            db.session.add(u)
            db.session.commit()
            login_user(u, remember=form.remember_me.data)
            return redirect(url_for('index'))
        except:
            flash('Такая почта уже зарегистрирована')
            return redirect(url_for('reg'))

    return render_template('registration.html', 
        title = 'Регистрация',
        form = form,
        )

@app.route('/auth', methods = ['GET', 'POST'])
def auth():
    users = models.User.query.all()
    for i in users:
        print (i.email,i.passwd)
    form = LoginForm()
    if form.validate_on_submit():
        #flash('Привет ' + form.login.data + '", remember_me=' + str(form.remember_me.data))
        u = db.session.query(User).filter(User.email == form.login.data).first()
        if u and u.check_password(form.password.data):
	        login_user(u, remember=form.remember_me.data)
	        return redirect(url_for('index'))

        flash('Что-то пошло не так , проверьте данные')
        return redirect(url_for('auth'))

    return render_template('login.html', 
        title = 'Войти',
        form = form,
        )

@app.route('/logout', methods = ['GET', 'POST'])
def logout():
    flash("")
    logout_user()
    return redirect(url_for('auth'))

@app.route('/timesheet', methods = ['GET', 'POST'])
def timesheet():
    return redirect(url_for('plug'))

@app.route('/takepass', methods = ['GET', 'POST'])
def takepass():
    return redirect(url_for('plug'))

@app.route('/doctor', methods = ['GET', 'POST'])
def doctor():
    return redirect(url_for('plug')) 

@app.route('/advice', methods = ['GET', 'POST'])
def advice():
    return redirect(url_for('plug'))    
   

#return redirect(url_for('auth'))
@app.route('/plug', methods = ['GET'])
def plug():
    return render_template('plug.html')