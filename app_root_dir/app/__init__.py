from .config import create_app
from .models import db, Profile
from flask_migrate import Migrate
from .views import register_routes
from .admin import create_admin

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

def initialize_database():
    if Profile.query.first() is None:
        default_profile = Profile(username="admin", password="admin")
        
        db.session.add(default_profile)
        db.session.commit()
        print("Perfil padrão criado: admin")
    else:
        print("Perfis existentes encontrados, nenhuma criação necessária.")