from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from config import DatabaseConfig
import mysql.connector

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nama = request.form['nama']
        email = request.form['email']
        password = request.form['password']
        alamat = request.form['alamat']

        # Simple validation
        if not nama or not email or not password:
            flash("Nama, Email, dan Password wajib diisi.", "danger")
            return redirect(url_for('auth.register'))

        try:
            conn = DatabaseConfig.get_connection()
            cursor = conn.cursor(dictionary=True)

            # Check if email already exists
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()

            if user:
                flash("Email sudah terdaftar.", "warning")
                return redirect(url_for('auth.register'))

            # Hash password
            password_hash = generate_password_hash(password)

            # Insert new user
            query = "INSERT INTO users (nama, email, password, alamat, role) VALUES (%s, %s, %s, %s, 'user')"
            cursor.execute(query, (nama, email, password_hash, alamat))
            conn.commit()

            flash("Registrasi berhasil! Silakan login.", "success")
            return redirect(url_for('auth.login'))

        except mysql.connector.Error as err:
            flash(f"Terjadi kesalahan database: {err}", "danger")
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()

    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            conn = DatabaseConfig.get_connection()
            cursor = conn.cursor(dictionary=True)

            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()

            if user and check_password_hash(user['password'], password):
                session['user_id'] = user['id']
                session['nama'] = user['nama']
                session['role'] = user['role']
                
                flash(f"Selamat datang, {user['nama']}!", "success")
                
                if user['role'] == 'admin':
                    return redirect(url_for('admin.dashboard')) # Assuming admin dashboard exists
                else:
                    return redirect(url_for('home')) # Or user dashboard

            else:
                flash("Email atau password salah.", "danger")

        except mysql.connector.Error as err:
            flash(f"Terjadi kesalahan database: {err}", "danger")
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()

    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash("Anda telah logout.", "info")
    return redirect(url_for('auth.login'))
