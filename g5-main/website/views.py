from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


# @views.route('/')
# def landing():
#     return render_template("landing.html")


@views.route('/')
@login_required
def home():
    return render_template("home.html", user= current_user)

def playerstats():
    return render_template("PlayerStats.html", user= current_user)

