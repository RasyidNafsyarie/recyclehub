from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from utils.decorators import login_required
from config import DatabaseConfig
import mysql.connector

pickup_bp = Blueprint('pickup', __name__)

@pickup_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        kategori = request.form['kategori']
        berat = request.form['berat']
        # Bank ID optional for now, or fetch from DB
        
        try:
            conn = DatabaseConfig.get_connection()
            cursor = conn.cursor()
            
            user_id = session['user_id']
            query = "INSERT INTO pickup_request (user_id, kategori, berat, status) VALUES (%s, %s, %s, 'pending')"
            cursor.execute(query, (user_id, kategori, berat))
            conn.commit()
            
            flash("Permintaan pickup berhasil dibuat!", "success")
            return redirect(url_for('pickup.status'))
            
        except mysql.connector.Error as err:
            flash(f"Error: {err}", "danger")
        finally:
            if 'cursor' in locals(): cursor.close()
            if 'conn' in locals(): conn.close()
            
    return render_template('pickup/create.html')

@pickup_bp.route('/status')
@login_required
def status():
    try:
        conn = DatabaseConfig.get_connection()
        cursor = conn.cursor(dictionary=True)
        
        user_id = session['user_id']
        query = "SELECT * FROM pickup_request WHERE user_id = %s ORDER BY created_at DESC"
        cursor.execute(query, (user_id,))
        requests = cursor.fetchall()
        
        return render_template('pickup/status.html', requests=requests)
        
    except mysql.connector.Error as err:
        flash(f"Error: {err}", "danger")
        return redirect(url_for('user.dashboard'))
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()
