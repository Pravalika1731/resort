from flask import Flask
from flask import render_template
import flask

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login.html")
def login():
    return render_template("login.html")

@app.route("/register.html")
def register():
    return render_template("register.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/services.html")
def service():
    return render_template("services.html")

@app.route("/index.html")
def index():
    return render_template("index.html")


@app.route("/login_form",methods=["post"])
def login_form():
    entered_name=flask.request.form.get("name")
    entered_pass=flask.request.form.get("password")
    import sqlite3
    con=sqlite3.connect("database.sqlite3")
    cur=con.cursor()
    table="create table if not exists user1table(name varchar(50),password varchar(50))"
    cur.execute(table)
    insert=f"insert into user1table values('{entered_name}','{entered_pass}')"
    cur.execute(insert)
    con.commit()
    return "registered successfully"

@app.route("/register_form",methods=["post"])
def register_form():
    entered_name=flask.request.form.get("name")
    entered_pass=flask.request.form.get("number")

    import sqlite3
    con=sqlite3.connect("database.sqlite3")
    cur=con.cursor()
    table="create table if not exists usertable(username varchar(50),password varchar(50))"
    cur.execute(table)
    insert=f"insert into usertable values('{entered_name}','{entered_pass}')"
    cur.execute(insert)
    con.commit()
    return "registered successfully"

if __name__=="__main__":
    app.run(debug=True)

