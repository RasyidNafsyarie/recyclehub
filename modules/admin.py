from flask import Blueprint, render_template, session
from utils.decorators import admin_required, login_required

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/dashboard')
@login_required
@admin_required
def dashboard():
    return render_template('admin/dashboard.html')
