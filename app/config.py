import logging
from flask import Flask

# Application log
logging.basicConfig(format='%(asctime)s - %(message)s', filename="log/app.log", level=logging.INFO)
log = logging.getLogger()

def create_app():
    app = Flask("Comp Dist")
    
    # Configuration
    app.config.from_pyfile('cfg/app.cfg', silent=True)
    app.config['FLASK_SECRET'] = app.config.get('SECRET_KEY')
    app.secret_key = app.config.get('SECRET_KEY')

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config.get('DATABASE')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Flask-Admin theme
    app.config['FLASK_ADMIN_SWATCH'] = 'yeti'
    
    return app
