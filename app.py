from flask import Flask, render_template, jsonify
from config import DatabaseConfig

# Import Blueprint
from modules.auth import auth_bp
from modules.user import user_bp
from modules.admin import admin_bp
from modules.pickup import pickup_bp

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secret123"

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(pickup_bp, url_prefix="/pickup")
    app.register_blueprint(admin_bp)

    @app.route("/")
    def home():
        return render_template("home.html")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
