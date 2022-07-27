from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task
# line 3 is importing from taskmanager folder, models.py,
# and is finding the 'Category and Task classes made in there


@app.route("/")
def home():
    return render_template("tasks.html")
