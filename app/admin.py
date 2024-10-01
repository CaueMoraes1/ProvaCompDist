from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask import redirect
from auth import validate_authentication, auth
from models import Profile
from werkzeug.exceptions import HTTPException
from flask import Response

class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(message, Response(
            "You could not be authenticated. Please refresh the page.", 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        ))

class MyModelView(ModelView):
    def is_accessible(self):
        if auth.get_auth():
            username = auth.get_auth()['username']
            password = auth.get_auth()['password']
        else:
            username, password = None, None

        if username and password and validate_authentication(username, password):
            return True
        raise AuthException('Not authenticated.')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(auth.login_required())

def create_admin(app, db):
    admin = Admin(app, name='Super App', template_mode='bootstrap4')
    admin.add_view(MyModelView(Profile, db.session))
