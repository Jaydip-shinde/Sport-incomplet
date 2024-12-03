from flask import Flask, request, jsonify, send_from_directory
import json
import random
import os
try:
    with open("spd.json", "r") as file:
        data = json.load(file)
    print("JSON file loaded successfully!")
except FileNotFoundError:
    print("File not found. Make sure the JSON file is in the correct location.")
except json.JSONDecodeError as e:
    print(f"JSON format error: {e}")
    
app = Flask(__name__, static_url_path="", static_folder=".")

# Load sports data from spd.json
JSON_PATH = "spd.json"
if not os.path.exists(JSON_PATH):
    raise FileNotFoundError(f"The file '{JSON_PATH}' is missing. Ensure it is in the correct location.")
else:
    with open(JSON_PATH) as f:
        sports_data = json.load(f)

def recommend_sport(data):
    age = int(data["age"])
    fitness = data["fitness"]
    sport_type = data["type"]
    time = data["time"]

    filtered_sports = [
        sport for sport in sports_data
        if sport["type"] == sport_type and sport["fitness"] == fitness and sport["time"] == time
    ]

    if not filtered_sports:
        return "Exploring New Sports", "Try something adventurous that suits your passion!"

    recommendation = random.choice(filtered_sports)
    return recommendation["name"], recommendation["description"]

@app.route("/")
def serve_html():
    return send_from_directory(".", "sport.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    sport, description = recommend_sport(data)
    return jsonify({"sport": sport, "description": description})

if __name__ == "__main__":
    app.run(debug=True)
