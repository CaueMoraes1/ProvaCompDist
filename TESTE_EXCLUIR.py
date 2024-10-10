import MySQLdb

try:
    connection = MySQLdb.connect(
        host="mysql_db",
        user="user",
        passwd="user_password",
        db="flask_app_db"
    )
    print("Conectado com sucesso ao MySQL!")
except MySQLdb.Error as err:
    print(f"Erro: {err}")
