import os
import sqlite3
from flask import Flask
from app.routes.main import bp as main_bp

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
app.secret_key = os.environ.get('SECRET_KEY', 'dev_secret_key')

# Register blueprints
app.register_blueprint(main_bp)

def init_db():
    db_path = os.path.join(app.instance_path, 'database.db')
    os.makedirs(app.instance_path, exist_ok=True)
    schema_path = os.path.join(os.path.dirname(__file__), 'database', 'schema.sql')
    
    with sqlite3.connect(db_path) as conn:
        with open(schema_path, 'r', encoding='utf-8') as f:
            conn.executescript(f.read())
    print("Database initialized successfully.")

if __name__ == '__main__':
    # Initialize DB for development purposes if it doesn't exist
    if not os.path.exists(os.path.join(app.instance_path, 'database.db')):
        init_db()
    app.run(debug=True)
