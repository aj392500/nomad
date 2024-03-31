   from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_input():
    data = request.json  # Get JSON data from the request
    # Process the input data (for demonstration, just echo it back)
    output_data = {'received_input': data}
    return jsonify(output_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
