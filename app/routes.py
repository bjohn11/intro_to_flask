from app import app, db
from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user

# Import for Forms
from app.forms import UserInfoForm, LoginForm

#Import for models 
from app.models import User

@app.route('/')
def index():
    context = {
        "customer_name" : "Brian",
        "customer_username" : "bjohn11",
        "items":{
            1: 'Ice Cream',
            2: 'Bread',
            3: 'Lemons',
            4: 'Cereal'
        }
    }
    return render_template('index.html', **context)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserInfoForm()
    context = {
        'form': form
    }
    if request.method== 'POST' and form.validate():
        # get information
        username = form.username.data
        password = form.password.data
        email = form.email.data

        # Create new instance of User
        new_user = User(username, email, password)

        #add user to db
        db.session.add(new_user)
        db.session.commit()

        #flash success message
        flash('Succesfully Registered', 'success')


        return redirect(url_for('index'))
    return render_template('register.html', **context)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    context = {
        'form' : form
    }
    if request.method== 'POST' and form.validate():
        email = form.email.data
        password = form.password.data

        # Query database for user with email
        user = User.query.filter_by(email=email).first()
        # if no user, flash incorrect credentials 
        if user is None or not check_password_hash(user.password, password):
            flash('Incorrect Email/Password. Please try again', 'danger')
            return redirect(url_for('login'))
        # else
        # log user in 
        login_user(user)
        # flash success message 
        flash('You have successfully logged in', 'success')
        return redirect(url_for('index'))
        


    return render_template('login.html', **context)