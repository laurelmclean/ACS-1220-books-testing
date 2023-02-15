from books_app.extensions import app, db
from books_app.main.routes import main
from books_app.auth.routes import auth

app.register_blueprint(main)
app.register_blueprint(auth)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host='localhost', port=8088, debug=True)
