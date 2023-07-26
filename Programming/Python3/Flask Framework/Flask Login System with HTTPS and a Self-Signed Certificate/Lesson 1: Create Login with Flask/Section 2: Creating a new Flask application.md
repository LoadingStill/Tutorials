## Section 2: Creating a new Flask application

```
pip install Flask
```

Once Flask is installed, create a new file called app.py in your project directory. This will be the main entry point for your Flask application. In app.py, import Flask and create a new instance of the Flask class like this:

```
from flask import Flask

app = Flask(__name__)
```

This will create a new Flask application with the name __name__. The __name__ argument is a special Python variable that tells Flask where to find resources like templates and static files.
