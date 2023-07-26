Storing user passwords in plain text is a major security risk. If a hacker gains access to your application's database, they can easily read all of the passwords and use them to gain access to other accounts. To prevent this, you should always hash user passwords before storing them in your database.

Flask provides several built-in functions for hashing passwords. To use them, you'll need to import the `generate_password_hash` and `check_password_hash` functions from the `werkzeug.security` module:

```
from werkzeug.security import generate_password_hash, check_password_hash
```
To hash a user's password before storing it in the database, you can use the `generate_password_hash` function. For example:

```
password = 'password123'
hashed_password = generate_password_hash(password)
```
This code generates a hash of the password using the default hashing algorithm (currently `pbkdf2:sha256`). You can then store this hashed password in your database.

To check if a user-entered password is correct, you can use the `check_password_hash` function. For example:

```
hashed_password = get_hashed_password_from_database()
password_attempt = request.form['password']

if check_password_hash(hashed_password, password_attempt):
    # Password is correct
else:
    # Password is incorrect
```
This code retrieves the hashed password from the database, retrieves the user-entered password from the form, and checks if the two passwords match using the `check_password_hash` function.

