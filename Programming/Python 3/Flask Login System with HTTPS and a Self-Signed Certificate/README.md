# Flask Login System with HTTPS and a Self-Signed Certificate

This is a Python Flask application that implements a simple login system with HTTPS enabled and a self-signed certificate. The login system accepts a username and password and sets a session variable to indicate that the user is logged in. The system uses Flask's built-in session management functionality to store the session data securely in a client-side cookie.

## Features

- HTTPS enabled with a self-signed certificate for secure communication
- Simple login system with username and password authentication
- Session management using Flask's built-in functionality
- Login and dashboard pages implemented using HTML and Flask's templating engine

## Installation

```sh
# Clone the repository to your local machine using Git:
git clone https://github.com/<username>/<repository-name>.git

# Alternatively, you can download the repository as a ZIP file and extract it to a directory of your choice.

# Install the required Python packages using pip:
pip install Flask pyopenssl cryptography

# Generate a self-signed SSL certificate using OpenSSL:
python generate_cert.py

# This will create a new file named server.crt that contains the SSL certificate, as well as a file named server.key that contains the private key.

# Start the Flask application by running the app.py script:
python app.py

# This will start the Flask application on https://localhost:5000.
```
  
Usage
1. Access the login page by visiting https://localhost:5000/login in a web browser. Note that because the SSL certificate is self-signed, your browser may display a warning message indicating that the connection is not secure. You can safely ignore this warning and proceed to the login page.
2. Enter a valid username and password to log in. By default, the application is configured with a single user account with the username "admin" and the password "password".
3. After successfully logging in, you will be redirected to the dashboard page. This page displays a welcome message and a link to log out.
4. To log out, click the "Log Out" link on the dashboard page. This will clear your session and redirect you back to the login page.
  
Disclaimer
This application is intended for educational purposes only and should not be used in a production environment without proper security measures in place. The self-signed SSL certificate is not suitable for use in a production environment and should only be used for development and testing purposes.








## Lesson 1: Create Login with Flask
1. Introduction to Flask
2. Creating a new Flask application
3. Creating a login page with Flask and HTML templates
4. Validating user input and authenticating users
5. Using Flask's session management to keep users logged in
6. Creating a dashboard page for authenticated users
7. Deploying the Flask application to a local server for testing

## Lesson 2: Add HTTPS with a Self-Signed Certificate
1. Introduction to HTTPS and SSL/TLS
2. Generating a self-signed SSL certificate using OpenSSL
3. Configuring a Flask application to use HTTPS
4. Testing the HTTPS-enabled Flask application in a local environment
5. Deploying the HTTPS-enabled Flask application to a server for production use.
