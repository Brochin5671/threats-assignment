from flask import Flask, request, jsonify
from flask_cors import CORS

from src import get_threats_data

# Setup app
app = Flask(__name__)
app.json.sort_keys = False
CORS(app, origins=['http://localhost:5173'])  # TODO: list origin differently


@app.get('/api/threats')
def get_threats():
    """Endpoint for getting a list of threats from urlhaus-api."""
    # Get query arguments and verify proper usage
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)
    if (page is None) != (limit is None):
        return jsonify({'error': 'Need to specify both page and limit query arguments.'}), 400

    # Only pass arguments that are not None
    args = [page, limit]
    data = get_threats_data(*[arg for arg in args if arg is not None])
    # Try to get the threats list data
    if data.get('error'):
        return jsonify(data), 500
    return jsonify(data)


# Runs the app if this file is ran
if __name__ == '__main__':
    app.run(debug=True)
