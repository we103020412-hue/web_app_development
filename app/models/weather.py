import sqlite3
import os

def get_db_connection():
    db_path = os.path.join('instance', 'database.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

class WeatherForecast:
    @staticmethod
    def get_forecasts(region_id=None, date=None, time_period=None):
        """根據條件取得天氣預報資料"""
        query = '''
            SELECT w.*, r.name as region_name 
            FROM weather_forecasts w
            JOIN regions r ON w.region_id = r.id
            WHERE 1=1
        '''
        params = []

        if region_id:
            query += ' AND w.region_id = ?'
            params.append(region_id)
        if date:
            query += ' AND w.forecast_date = ?'
            params.append(date)
        if time_period:
            query += ' AND w.time_period = ?'
            params.append(time_period)

        query += ' ORDER BY w.forecast_date ASC, w.region_id ASC'

        try:
            with get_db_connection() as conn:
                return conn.execute(query, params).fetchall()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
