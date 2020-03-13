from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, logout_user, login_required, login_user

from Blogger.users.models import User
from .forms import LoginForm, RegistrationForm

auth_app = Blueprint('auth_app', __name__)


@auth_app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('users_app.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.find_user_by_email(form.email.data)
        if user and user.check_password(form.password.data):
            login_user(user, remember=False)
            return redirect(url_for('users_app.dashboard'))
        else:
            flash(message="Invalid email or password", category='is-danger')

    return render_template('auth/login.html', form=form)


@auth_app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('users_app.dashboard'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User({
            'name': form.name.data.title(),
            'email': form.email.data,
            'password': form.password.data
        })
        user.save_to_db()
        flash(message="You are now registered, Please login", category="is-success")
        return redirect(url_for('auth_app.login'))

    return render_template('auth/register.html', form=form)


@auth_app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_app.login'))
