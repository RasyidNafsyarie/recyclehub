import mysql.connector
from mysql.connector import pooling

class DatabaseConfig:
    DB_CONFIG = {
        "host": "localhost",
        "user": "root",
        "password": "",
        "database": "recyclehub"
    }

    POOL = pooling.MySQLConnectionPool(
        pool_name="recyclehub_pool",
        pool_size=5,
        **DB_CONFIG
    )

    @staticmethod
    def get_connection():
        return DatabaseConfig.POOL.get_connection()
