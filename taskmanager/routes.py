from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task
# line 3 is importing from taskmanager folder, models.py,
# and is finding the 'Category and Task classes made in there


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")


@app.route("/add_category", methods=["GET", "POST"])
# get and post , needed because it's submitting a form
def add_category():
    return render_template("add_category.html")
