from config import create_app
from models import db
from flask_migrate import Migrate
from views import register_routes
from admin import create_admin

def create_all():
    app = create_app()
    
    # Initialize database
    db.init_app(app)
    migrate = Migrate(app, db)

    # Register routes
    register_routes(app)

    # Initialize admin interface
    create_admin(app, db)

    return app
