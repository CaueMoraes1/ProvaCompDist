import logging
from flask import Flask
import MySQLdb

# Application log
logging.basicConfig(format='%(asctime)s - %(message)s', filename="./log/app.log", level=logging.INFO)
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
    

    try:
        # Conexão com o MySQL usando o nome do serviço 'db' como host
        connection = MySQLdb.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            passwd=app.config['MYSQL_PASSWORD'],
            db=app.config['MYSQL_DB']
        )
        app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{app.config['MYSQL_USER']}:{app.config['MYSQL_PASSWORD']}@{app.config['MYSQL_HOST']}/{app.config['MYSQL_DB']}"
        print("Conexão MySQL estabelecida com sucesso!")
    except MySQLdb.Error as e:
        # Fallback para SQLite
        app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{app.config['SQLITE_DB_PATH']}"
        print(f"Erro na conexão com MySQL: {e}")
        print(f"Usando SQLite como fallback. Dados salvos em {app.config['SQLITE_DB_PATH']}")


    # Flask-Admin theme
    app.config['FLASK_ADMIN_SWATCH'] = 'yeti'
    
    return app
