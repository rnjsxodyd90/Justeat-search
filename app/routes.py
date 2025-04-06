from flask import Blueprint, render_template
from .utils import get_restaurants

# Creating a Blueprint for main routes ( Flask structure)

main = Blueprint('main', __name__)
# Define the route for the homepage

@main.route("/")
def index():
    postcode = "M160RA"
    restaurants = get_restaurants(postcode)
    # Render the HTML template and pass restaurant data to it
    return render_template("index.html", restaurants=restaurants)