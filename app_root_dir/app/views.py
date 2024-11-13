from flask import jsonify
from flask_admin.contrib.sqla import ModelView
from .models import Profile
from .auth import auth
from .config import log

def register_routes(app):
    @app.route('/')
    @auth.login_required
    def index():
        user = auth.current_user()
        user_db = Profile.query.filter_by(username=user).first()

        if user_db:
            message_info = f"Usuário {user}, acessou o index."
            response = {"success": message_info}
            log.info(message_info)
            return jsonify(response)

class UserAdmin(ModelView):
    """Classe de administracao de user"""