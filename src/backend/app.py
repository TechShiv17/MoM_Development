from flask import Flask,request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/recording-link', methods=['POST'])
def get_recording_link():
    # recording_link = 'fsdfasf'
    recording_link = request.args.get('link')
    if recording_link is not None:
        return jsonify({'link': recording_link})
    else:
        response = jsonify({'error': 'Unauthorized: Missing or invalid token'})
        response.status_code = 400
        return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)