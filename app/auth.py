from werkzeug.security import generate_password_hash, check_password_hash
from .models import Profile
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    user = Profile.query.filter_by(username=username).first()
    if user and check_password_hash(generate_password_hash(user.password), password):
        return username

def validate_authentication(username, password):
    user = Profile.query.filter_by(username=username).first()
    if user and user.password == password:
        return True
    return False
