from flask import Blueprint, render_template
from .utils import get_restaurants

main = Blueprint('main', __name__)

@main.route("/")
def index():
    postcode = "M160RA"
    restaurants = get_restaurants(postcode)
    return render_template("index.html", restaurants=restaurants)