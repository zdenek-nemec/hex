from flask import Flask, request, jsonify

app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok"},
    {"id": 2, "name": "Australia", "capital": "Canberra"},
    {"id": 3, "name": "Egypt", "capital": "Cairo"}
]

def _find_next_id():
    return max(country["id"] for country in countries) + 1

@app.get("/countries")
def get_countries():
    return jsonify(countries)

@app.post("/countries")
def add_country():
    if request.is_json:
        new_country = request.get_json()
        new_country["id"] = _find_next_id()
        countries.append(new_country)
        return jsonify(new_country), 201
    return {"error": "Request must be JSON"}, 415

@app.get("/countries/<int:id>")
def get_country(id):
    country = next((c for c in countries if c["id"] == id), None)
    if country:
        return jsonify(country)
    return {"error": "Country not found"}, 404

if __name__ == "__main__":
    app.run(debug=True)
