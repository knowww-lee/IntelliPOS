import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
    "port": int(os.getenv("DB_PORT", 3306)),  # Default to 3306 if not set
}

def connect_db():
    """Create and return a secure database connection."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        print("✅ Database Connected Successfully!")
        return conn
    except mysql.connector.Error as err:
        print(f"❌ Database Connection Error: {err}")
        return None
