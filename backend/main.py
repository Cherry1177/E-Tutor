from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/api/v1/user")
def get_all_users():
    return "<p>Here are all the users</p>"


@app.route("/api/v1/user/<id>")
def get_one_user_by_id(id):
    return "Here is the user with id: " + id
