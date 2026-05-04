import sqlite3
import os

def get_db_connection():
    db_path = os.path.join('instance', 'database.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

class Region:
    @staticmethod
    def get_all():
        """取得所有地區"""
        try:
            with get_db_connection() as conn:
                return conn.execute('SELECT * FROM regions').fetchall()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []

    @staticmethod
    def get_by_id(region_id):
        """根據 ID 取得特定地區"""
        try:
            with get_db_connection() as conn:
                return conn.execute('SELECT * FROM regions WHERE id = ?', (region_id,)).fetchone()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
