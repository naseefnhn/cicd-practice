import sqlite3

def get_user(username):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Do the string formatting INLINE inside the execute() function.
    # Semgrep rules specifically look for this pattern!
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    
def add(a, b):
    return a + b

