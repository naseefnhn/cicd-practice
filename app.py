def get_user_query(username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return query

def add(a, b):
    return a + b