from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_restaurants(postcode):
    url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
    headers = {
        "Accept-Tenant": "uk",
        "Accept-Language": "en-GB",
        "Accept": "application/json",
        "User-Agent": "JustEat-Client"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        restaurants = data.get("restaurants", [])[:10]

        result = []
        for r in restaurants:
            result.append({
                "name": r.get("name", "N/A"),
                "cuisines": ", ".join([c["name"] for c in r.get("cuisines", [])]),
                "rating": r.get("rating", {}).get("starRating", "N/A"),
                "address": r.get("address", {}).get("firstLine", "") + ", " + r.get("address", {}).get("postalCode", "")
            })

        return result

    except Exception as e:
        print(f"Error: {e}")
        return []

@app.route('/')
def index():
    postcode = "M160RA"
    restaurants = get_restaurants(postcode)
    return render_template("index.html", restaurants=restaurants)

if __name__ == "__main__":
    app.run(debug=True)
