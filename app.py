from flask import Flask, jsonify, render_template
from config import DatabaseConfig

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secret123"  # ganti sesuai kebutuhan

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

    # === Home Page ===
    @app.route("/")
    def home():
        return render_template("home.html")

    # === Test Database Connection ===
    @app.route("/db-test")
    def db_test():
        try:
            conn = DatabaseConfig.get_connection()
            cursor = conn.cursor(dictionary=True)

            cursor.execute("SELECT NOW() AS waktu_server;")
            result = cursor.fetchone()

            cursor.close()
            conn.close()

            return jsonify({
                "status": "connected",
                "server_time": result["waktu_server"]
            })

        except Exception as e:
            return jsonify({
                "status": "error",
                "message": str(e)
            })

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
