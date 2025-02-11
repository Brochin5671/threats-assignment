from flask import Flask, request, jsonify

from src import get_threats_data

# Setup app
app = Flask(__name__)
app.json.sort_keys = False


@app.get('/api/threats')
def get_threats():
    page = request.args.get('page')
    limit = request.args.get('limit')
    if bool(page) != bool(limit):
        return jsonify({'message': 'Need to specify both page and limit query arguments.'}), 400

    # TODO: Handle errors and pagination
    threats = get_threats_data()
    return jsonify({'threats': threats})


# Runs the app if this file is ran
if __name__ == '__main__':
    app.run(debug=True)
