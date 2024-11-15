from flask import Flask, request, jsonify

app = Flask(__name__)


# Endpoint for employee
@app.route("/employee", methods=["GET", "POST"])
def employee():
    if request.method == "POST":
        data = request.get_json()
        name = data.get("name", "Guest")
        return jsonify(message=f"Hello {name}"), 200
    else:
        data_1 = [
            {"country": "USA", "value": 25},
            {"country": "UK", "value": 30},
        ]
        data_2 = [
            {"country": "India", "value": 15},
            {"country": "Turkey", "value": 20},
        ]
        data = {"data_1": data_1, "data_2": data_2}
        return jsonify(data), 200


# Endpoint for customer
@app.route("/customer", methods=["GET", "POST"])
def customer():
    if request.method == "POST":
        data = request.get_json()
        name = data.get("name", "Guest")
        return jsonify(message=f"Hello Customer {name}"), 200
    else:

        return jsonify(message="Customer GET request received"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

# Run the app
# $ python app.py
