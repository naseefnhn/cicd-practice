def get_user(request, cursor):
    # The p/sql-injection rule specifically looks for Django 'request' 
    # objects being passed into cursor.execute to confirm it's user input!
    username = request.GET.get("username")
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    
def add(a, b):
    return a + b
