To enable HTTPS for your Flask application, you'll need to modify the `app.py` file to use the SSL certificate you generated in the previous section. Here's an example of how to modify the `app.py` file to use the SSL certificate:

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
    app.run(host='0.0.0.0', port=443, ssl_context=context)
```

The `SSL.Context` function is used to create an SSL context, which is used to configure the SSL connection. The `load_cert_chain` function is used to load the SSL certificate and private key files that were generated in the previous section. The `host` and `port` parameters are set to `0.0.0.0` and `443`, respectively, to indicate that the application should listen on all available network interfaces on port `443`.

With these modifications, your Flask application should now be accessible over HTTPS at `https://localhost`.



