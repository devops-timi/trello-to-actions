from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health():
    """Check if the API is running. Returns status UP."""
    return jsonify({"status": "UP"}), 200


@app.route('/sum', methods=['POST'])
def get_sum():
    """
    Accept two numbers a and b in JSON body.
    Returns their sum. Returns 400 if inputs are not numeric.
    """
    data = request.get_json()
    a = data.get('a', 0)
    b = data.get('b', 0)
    if not isinstance(a, (int, float)):
        return jsonify({"error": "Invalid input"}), 400
    if not isinstance(b, (int, float)):
        return jsonify({"error": "Invalid input"}), 400
    result = a + b
    return jsonify({"result": result})


@app.route('/reverse-string', methods=['POST'])
def reverse_string():
    """
    Accept a string text in JSON body.
    Returns the reversed string.
    """
    data = request.get_json()
    text = data.get('text', "")
    return jsonify({"result": text[::-1]})


if __name__ == '__main__':
    app.run()

