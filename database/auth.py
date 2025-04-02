import bcrypt
from database.db_config import connect_db

def hash_password(password):
    """Hash a password before storing it in the database."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)

def verify_password(stored_password, provided_password):
    """Verify the provided password against the stored hashed password."""
    return bcrypt.checkpw(provided_password.encode(), stored_password.encode())

def authenticate_user(username, password):
    """Check user credentials securely."""
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            query = "SELECT username, password FROM users WHERE username = %s"
            cursor.execute(query, (username,))
            user = cursor.fetchone()
            
            if user and verify_password(user['password'], password):
                return True  # Login successful
            else:
                return False  # Invalid credentials

        except Exception as err:
            print(f"Authentication Error: {err}")
        finally:
            cursor.close()
            conn.close()
    
    return False
