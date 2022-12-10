from flask import Flask
from flask import Blueprint, request, redirect, render_template, url_for

from functools import wraps
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from utils import LoginForm, User
from db import accountdb

auth = Blueprint('auth', __name__)

def check_login(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated: 
            return redirect(url_for('main'))
        return f(*args, **kwargs)
    return wrapper

@auth.route('/login', methods=['GET', 'POST'])
def login():
    print(current_user)
    if current_user.is_authenticated: 
        return redirect(url_for('staff.main'))
    
    form = LoginForm()
    if request.method=='POST':
        if form.validate():
            id = form.id.data
            password = form.password.data
            loginInfo = accountdb.login(id, password, "STAFF")
            if "Login successfully!" in loginInfo:
                username = accountdb.findUserName(id)
                login_user(User(id, username, "STAFF"))
                return redirect(url_for('staff.main'))
            elif "Wrong Password!" in loginInfo:
                return render_template('login.html')
            else:
                return render_template('login.html')

    return render_template('login.html')