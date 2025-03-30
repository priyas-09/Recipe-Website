from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    query = request.args.get("q", "Chicken")
    api_url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={query}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        recipes = data.get("meals")
    else:
        recipes = None
    return render_template("index.html", recipes=recipes, query=query)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
# This is a simple Flask application that fetches recipes from TheMealDB API based on a search query.