from flask import Flask, render_template, request, redirect, url_for
from data_manager import DataManager
from models import db, Movie

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

data_manager = DataManager()


@app.route("/")
def index():
    users = data_manager.get_users()
    return render_template("index.html", users=users)


@app.route("/users", methods=["POST"])
def create_user():
    name = request.form.get("name")
    if name:
        data_manager.create_user(name)
    return redirect(url_for("index"))


@app.route("/users")
def list_users():
    users = data_manager.get_users()
    return str(users)


@app.route("/users/<int:user_id>/movies", methods=["GET"])
def user_movies(user_id):
    return f"Movies page for user {user_id}"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)