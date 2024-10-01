from app import create_all

app = create_all()

if __name__ == "__main__":
    with app.app_context():
        app.run(host="0.0.0.0", debug=True, port=8080)
