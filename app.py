from flask import Flask, render_template
from config import Config
import mysql.connector
from flask import g

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB
        )
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

    app.teardown_appcontext(close_db)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # === Import Blueprint ===
    from modules.auth import auth_bp
    from modules.user import user_bp
    from modules.admin import admin_bp
    from modules.pickup import pickup_bp

    # === Register Blueprint ===
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(pickup_bp)

    @app.route("/")
    def home():
        return render_template("home.html")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
