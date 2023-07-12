To ensure that all traffic to your Flask application is secure, you can configure your application to redirect HTTP traffic to HTTPS. This can be done by adding a separate `app.run` command for HTTP traffic, which simply redirects incoming requests to the HTTPS version of the site.

Here's an example of how to add HTTP to HTTPS redirect to your Flask application:

```
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import os
from OpenSSL import SSL

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def home():
    return render_template('home.html')

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

@app.route('/dashboard')
def dashboard():
    # Check if the user is logged in
    if 'logged_in' in session and session['logged_in']:
        return render_template('dashboard.html')
    else:
        # If the user is not logged in, redirect to the login page
        return redirect(url_for('login'))

if __name__ == '__main__':
    context = SSL.Context(SSL.PROTOCOL_TLSv1_2)
    context.load_cert_chain('server.crt', 'server.key')
    app.run(host='0.0.0.0', port=443, ssl_context=context, threaded=True)

    # Redirect HTTP traffic to HTTPS
    app.run(host='0.0.0.0', port=80, threaded=True, debug=True, ssl_context='adhoc')
```
In this example, an additional `app.run` command is added to the bottom of the file to listen for HTTP traffic on port `80`. The `debug` parameter is set to `True` to enable Flask's debugging mode, and the `ssl_context` parameter is set to 'adhoc' to indicate that Flask should generate a temporary SSL certificate for this connection.

With these modifications, your Flask application should now redirect all HTTP traffic to HTTPS, ensuring that all traffic to your site is secure.
