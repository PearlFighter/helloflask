from flask import Flask, json
from datetime import datetime
from flask import render_template
from flask import Flask
from flask import request
import re

app = Flask(__name__)

# Replace the existing home function with the one below
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")


companies = [{"id": 1, "name": "Company One"}, {"id": 3, "name": "Company Two"}]

@app.route('/companies', methods=['GET'])
def get_companies():
  return json.dumps(companies)

@app.route('/companies', methods=['POST'])
def post_companies():
    print (request.is_json)
    content = request.get_json()
    print (content)
    return json.dumps({"success": True}), 201



