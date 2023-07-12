from flask import Flask, render_template, request, session, redirect, url_for
from OpenSSL import crypto, SSL
from cryptography.x509 import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
import os

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Generate a self-signed certificate
def generate_self_signed_cert():
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    subject = issuer = crypto.X509Name([(NameOID.COMMON_NAME, u"localhost")])
    cert = crypto.X509()
    cert.set_subject(subject)
    cert.set_issuer(issuer)
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(10 * 365 * 24 * 60 * 60)
    cert.set_pubkey(key.public_key())
    cert.sign(key, "sha256")
    with open(os.path.join(os.getcwd(), "key.pem"), "wb") as f:
        f.write(key.private_bytes(encoding=crypto.FILETYPE_PEM, format=crypto.PKCS8, encryption_algorithm=crypto.NoEncryption()))
    with open(os.path.join(os.getcwd(), "cert.pem"), "wb") as f:
        f.write(cert.public_bytes(encoding=crypto.FILETYPE_PEM))
generate_self_signed_cert()

# Configure Flask to use HTTPS
context = SSL.Context(SSL.TLSv1_2_METHOD)
context.use_privatekey_file(os.path.join(os.getcwd(), "key.pem"))
context.use_certificate_file(os.path.join(os.getcwd(), "cert.pem"))

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')

# Dashboard route
@app.route('/dashboard')
def dashboard():
    if session.get('logged_in'):
        return render_template('dashboard.html')
    else:
        return redirect(url_for('login'))

# Logout route
@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True, ssl_context=context)
