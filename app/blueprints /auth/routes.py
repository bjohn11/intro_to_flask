from . import bp as auth, mail, Message
from flask import request, url_for, render_template, redirect, flash
from app import db
from werkzeug.security import check_password_hash
from flask_login import current_user, login_required, logout_user, login_user

from app.models import User
from app.forms import UserInfoForm, LoginForm


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = UserInfoForm()
    context = {
        'form': form
    }
    if request.method == 'POST' and form.validate():
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

        #Flask email Sender
        msg = Message(
            f'Thanks for signing up, {username}!', recipients=[email])
        msg.body = ('Congrats on signing up! I hope you enjoy our site!!')
        msg.html = (
            '<h1> Welcome to Our Site</h1>' '<p> This will be super cool!</p>')

        mail.send(msg)

        return redirect(url_for('index'))
    return render_template('register.html', **context)
 
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    context = {
        'form': form
    }
    if request.method == 'POST' and form.validate():
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
        login_user(user, remember=form.remember_me.data)
        # flash success message
        flash('You have successfully logged in', 'success')
        return redirect(url_for('index'))

    return render_template('login.html', **context)


@auth.route('/logout')
def logout():
    logout_user()
    flash('You have successfully logged out', 'primary')
    return redirect(url_for('index'))



