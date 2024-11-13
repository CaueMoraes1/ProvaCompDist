from app import create_all, initialize_database
from app.models import db
from app.views import UserAdmin

    
app = create_all()



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        initialize_database()
        app.run(host="0.0.0.0", debug=True, port=8080)
