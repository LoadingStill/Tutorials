from OpenSSL import crypto
from cryptography.x509 import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
import os

# Generate a new RSA private key
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Create a self-signed certificate
subject = issuer = crypto.X509Name([(NameOID.COMMON_NAME, u"localhost")])
cert = crypto.X509()
cert.set_subject(subject)
cert.set_issuer(issuer)
cert.set_serial_number(1000)
cert.gmtime_adj_notBefore(0)
cert.gmtime_adj_notAfter(10 * 365 * 24 * 60 * 60)
cert.set_pubkey(key.public_key())
cert.sign(key, "sha256")

# Write the key and certificate to disk
with open(os.path.join(os.getcwd(), "key.pem"), "wb") as f:
    f.write(key.private_bytes(encoding=crypto.FILETYPE_PEM, format=crypto.PKCS8, encryption_algorithm=crypto.NoEncryption()))
with open(os.path.join(os.getcwd(), "cert.pem"), "wb") as f:
    f.write(cert.public_bytes(encoding=crypto.FILETYPE_PEM))

    
    
#In this example, we are generating a new 2048-bit RSA private key and using it to create a self-signed certificate with a validity period of 10 years.
#We are then writing the key and certificate to disk as key.pem and cert.pem, respectively.
#You can run this script to generate a new self-signed certificate for use in your Flask application.
#Note that this script should only be run once to generate the certificate, and not every time you run your Flask application.
