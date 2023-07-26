Flask provides a built-in session management system that allows you to store data securely in a client-side cookie. This makes it easy to keep track of whether a user is logged in or not.

To use Flask's session management functionality, you'll need to import the session object from Flask:

```
from flask import session
```
This object allows you to store data securely in a client-side cookie. To set a session variable to indicate that the user is logged in, modify the login function as follows:

```
from flask import render_template, request, redirect, url_for, session

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username and password are valid
        if username == 'admin' and password == 'password':
            # Set the session variable to indicate that the user is logged in
            session['logged_in'] = True
            
            # Redirect the user to the dashboard page
            return redirect(url_for('dashboard'))
        else:
            # If the username or password is incorrect, display an error message
            error = 'Invalid credentials. Please try again.'
            return render_template('login.html', error=error)
    
    # If the request method is GET, render the login page
    return render_template('login.html')
```
This code sets a session variable called `logged_in` to `True` when the user successfully logs in. This session variable is stored securely in a client-side cookie and can be accessed from any page in the application.

To check whether a user is logged in on other pages, you can simply check the value of the `session['logged_in']` variable. For example, to create a dashboard page that can only be accessed by logged-in users, you can modify the `dashboard` function as follows:

```
@app.route('/dashboard')
def dashboard():
    # Check if the user is logged in
    if not session.get('logged_in'):
        # If the user is not logged in, redirect to the login page
        return redirect(url_for('login'))
    
    # If the user is logged in, render the dashboard page
    return render_template('dashboard.html')
 ```
This code checks if the `session['logged_in']` variable is set to `True`. If it is not, the code redirects the user to the login page. If the user is logged in, the code renders the `dashboard.html` template. This ensures that only logged-in users can access the dashboard page.

