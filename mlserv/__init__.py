from flask import Flask
# Import CSRFProtect (Cross-Site Request Forgery Protection) object
from flask_wtf.csrf import CSRFProtect
# Import Bootstrap, an open source CSS framework
from flask_bootstrap import Bootstrap
from keras.models import load_model
import os

# Instantiate CSRF Protection object
csrf = CSRFProtect()
# Instantiate the Flask object used to run the web server
app = Flask(__name__)
# Automatically reload templates if one is edited and saved.
# Allows for dynamic template updates without a server restart.
app.config['TEMPLATES_AUTO_RELOAD'] = True
# Add a cryptographically secure, randomized secret key used for form validation.
app.config['SECRET_KEY'] = os.urandom(32)

# Apply the app to the Bootstrap and CSRF objects.
Bootstrap(app)
csrf.init_app(app)

model = load_model('./dog_cat.h5')
from mlserv import views