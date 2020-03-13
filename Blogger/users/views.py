from flask import Blueprint, render_template
from flask_login import login_required

users_app = Blueprint('users_app', __name__)


@users_app.route('/account')
@login_required
def account():
    return render_template('users/account.html')


@users_app.route('/dashboard')
@login_required
def dashboard():
    return render_template('users/dashboard.html')
