HTTP Strict Transport Security (HSTS) is a security feature that instructs web browsers to always connect to a website over HTTPS, even if the user types in an HTTP URL. This helps prevent attackers from intercepting or tampering with the user's connection to the website.

To enable HSTS for your Flask application, you can use the `flask-talisman` package. Here's an example of how to install and use the `flask-talisman` package in your Flask application:

Install the flask-talisman package using pip:

```
pip install flask-talisman
```

Modify your app.py file to enable HSTS using the flask-talisman package:

```
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import os
from OpenSSL import SSL
from flask_talisman import Talisman

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Enable HSTS
Talisman(app, force_https=True)

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
In this example, the `Talisman` object is created and initialized with the `app` object to enable HSTS. The `force_https` parameter is set to `True` to instruct web browsers to always connect to the site over HTTPS.

With these modifications, your Flask application should now be even more secure with the added protection of HSTS.
