from flask import Flask, request, jsonify
from flask_cors import CORS

from src import get_threats_data

# Setup app
app = Flask(__name__)
app.json.sort_keys = False
CORS(app, origins=['http://localhost:5173'])


@app.get('/api/threats')
def get_threats():
    # Get query arguments and verify proper usage
    page = request.args.get('page')
    limit = request.args.get('limit')
    if bool(page) != bool(limit):
        return jsonify({'error': 'Need to specify both page and limit query arguments.'}), 400

    # TODO: Handle pagination
    # Try to get the threats list data
    data = get_threats_data()
    if data.get('error'):
        return jsonify(data), 500
    return jsonify(data)


# Runs the app if this file is ran
if __name__ == '__main__':
    app.run(debug=True)
