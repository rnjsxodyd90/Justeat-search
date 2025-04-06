import requests
import json


def get_restaurants(postcode):
    url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
    headers = {
        "Accept-Tenant": "uk",
        "Accept-Language": "en-GB",
        "Accept": "application/json",
        "User-Agent": "JustEat-Client"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        restaurants = data.get("restaurants", [])[:10]
        result = []

        for r in restaurants:
            cuisine_names = [c["name"] for c in r.get("cuisines", [])]

            # Mapping national cuisines to flags
            nationality_flags = {
                "Italian": "🇮🇹",
                "Indian": "🇮🇳",
                "American": "🇺🇸",
                "Turkish": "🇹🇷",
                "Chinese": "🇨🇳",
                "Japanese": "🇯🇵",
                "Mexican": "🇲🇽",
                "Thai": "🇹🇭",
                "Greek": "🇬🇷",
                "Korean": "🇰🇷"
                                }

            # Get first matched nationality (if any)
            national_cuisine = next((c for c in cuisine_names if c in nationality_flags), None)
            national_flag = nationality_flags.get(national_cuisine)

            result.append({
                "name": r.get("name", "N/A"),
                "cuisines": cuisine_names,  #instead of combining cuisines to a single string, kept them as a list to have access individually in the html
                "delivery_cost": r.get("deliveryCost", None),

                "rating": r.get("rating", {}).get("starRating", "N/A"),
                "address": r.get("address", {}).get("firstLine", "") + ", " + r.get("address", {}).get("postalCode", ""),
                "halal": "Halal" in cuisine_names,
                "flag": national_flag,
                "nationality": national_cuisine
            })

        return result

    except Exception as e:
        print(f"Error: {e}")
        return []



