from flask import render_template, redirect, url_for, jsonify
from settings.app import app


@app.route("/", methods=["GET"])
def login_page():
    return render_template("login.html")

@app.route("/", methods=["POST"])
def login_page_post():
    return redirect("http://localhost:3000")

@app.route("/success")
def success_page():
    return jsonify({"message": "Success!"})

