from flask import render_template, redirect, url_for, jsonify, request
from settings.app import app, google    
from models import User


@app.route("/", methods=["GET"])
def login_page():
    return render_template("login.html")

@app.route("/", methods=["POST"])
def login_page_post():

    user = User(request.form["identifier"])

    if user.verify(request.form["password"]):
        return redirect("http://localhost:3000")
    
    return redirect(url_for("login_page"))

@app.route("/success")
def success_page():
    return jsonify({"message": "Success!"})

@app.route("/google", methods=["POST"])
def login_google():
    return google.authorize(callback=url_for('login_google_authorized', _external=True))
    
@app.route('/google/authorized')
def login_google_authorized():
    return redirect("http://localhost:3000")

