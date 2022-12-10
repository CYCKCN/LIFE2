from flask import Flask
from flask import Blueprint, request, redirect, render_template, url_for

from functools import wraps
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from utils import User
from db import accountdb

auth = Blueprint('auth', __name__)

# def check_login(f):
#     @wraps(f)
#     def wrapper(*args, **kwargs):
#         if not current_user.is_authenticated: 
#             return redirect(url_for('staff.home'))
#         return f(*args, **kwargs)
#     return wrapper

@auth.route('/login', methods=['GET', 'POST'])
def login():

    # if current_user.is_authenticated: 
    #     return redirect(url_for('staff.home'))
    
    if request.method == 'POST':
        # id = request.form['nm']
        # id = request.form['username']
        id = request.form.get('username')
        password = request.form.get('password')
        submit = request.form.get('submit-button')

        print(id, password, submit)

        if submit == "Submit": 
            loginInfo = accountdb.login(id, password, "STAFF")
            print(loginInfo)
            if "Login successfully!" in loginInfo:
                username = accountdb.findUserName(id)
                login_user(User(id, username, "STAFF"))
                return redirect(url_for('staff.home'))

    return render_template('login.html')