from flask import Blueprint, render_template, session
from utils.decorators import login_required

user_bp = Blueprint('user', __name__)

@user_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('user/dashboard.html')
