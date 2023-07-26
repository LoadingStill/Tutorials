To enable HTTPS for your Flask application, you'll need to generate a SSL certificate. You can generate a self-signed SSL certificate using the `generate_cert.py` script included in this project. Here's the code for that script:

```
from OpenSSL import crypto, SSL
import os

def create_self_signed_cert():
    # Create a key pair
    k = crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, 2048)

    # Create a self-signed certificate
    cert = crypto.X509()
    cert.get_subject().C = "US"
    cert.get_subject().ST = "CA"
    cert.get_subject().L = "San Francisco"
    cert.get_subject().O = "Flask Login System"
    cert.get_subject().OU = "IT Department"
    cert.get_subject().CN = "localhost"
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(315360000)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(k)
    cert.sign(k, 'sha256')

    # Save the key and certificate to disk
    with open("server.crt", "wt") as f:
        f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode("utf-8"))
    with open("server.key", "wt") as f:
        f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k).decode("utf-8"))

if __name__ == '__main__':
    create_self_signed_cert()
```
This code uses the `OpenSSL` library to generate a self-signed SSL certificate. The certificate is valid for 10 years (`315360000` seconds) and is issued to `localhost`. The private key and certificate are saved to disk as `server.key` and `server.crt`, respectively.

To generate a self-signed SSL certificate for your Flask application, run the `generate_cert.py` script:

```
python generate_cert.py
```
This will create a self-signed SSL certificate in the current directory. You can then use this certificate to enable HTTPS for your Flask application.
