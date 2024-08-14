import flask
import random
import sqlite3

r = random
f = flask
app = flask.Flask(__name__)

@app.route("/menu/")
def results():
    connect = sqlite3.connect("datamenu.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM menu")
    data = cursor.fetchall()
    return flask.render_template("menu.html", data=data)

@app.route("/main_page/")
def main_page():
    return f.render_template("something.html", title="Pizzaria")

@app.route("/")
def start():
    return f.render_template("login.html", title="Login")

@app.route("/add_pizza/", methods=['GET', 'POST'])
def add_pizza():
    if flask.request.method == "POST":
        name = flask.request.form["name"]
        ingredients = flask.request.form["ingredients"]
        price = flask.request.form["price"]
        with sqlite3.connect("datamenu.db") as user:
            cursor = user.cursor()
            cursor.execute("INSERT INTO MENU \
            (name,ingredients,price) VALUES (?,?,?)",
                           (name, ingredients, price)),
            user.commit()
        return flask.render_template("add_pizza.html")
    else:
        return flask.render_template("add_pizza.html")

app.run(port=55555, debug=True)