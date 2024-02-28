# Name : Siva Rama Rohan Sunkarapalli
# Section : CS591
# Homework : 5

from flask import Flask, jsonify, request

app = Flask(__name__)

countries = ["United States", "Canada", "Mexico", "United Kingdom", "France", "Germany", "Australia", "Japan", "China", "Russia"]

@app.route('/api/greeting', methods=['GET'])
def greeting():
    name = request.args.get('name', 'world')
    return jsonify({"message": f"Hello, {name}!"})

@app.route('/api/sum', methods=['GET'])
def sum_numbers():
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        result = a + b
        return jsonify({"result": result})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please provide valid integers 'a' and 'b'."})

# Add the countries endpoint
@app.route('/api/countries', methods=['GET'])
def get_countries():
    return jsonify({"countries": countries})

if __name__ == '__main__':
    app.run(debug=True)
