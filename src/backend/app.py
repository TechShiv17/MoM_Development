from flask import Flask, request, jsonify
from flask_cors import CORS
from src.app.main import MoMGenerator

app = Flask(__name__)
CORS(app)


@app.route('/recording-link', methods=['POST'])
def get_recording_link():
    recording_link = request.args.get('link')
    if recording_link is not None:
        MoMGenerator.processVideo(recording_link)
        response = jsonify({'message': 'Success', 'status_code': 200})
        return response
    else:
        response = jsonify({'message': 'Unauthorized: Missing or invalid token', 'status_code': 400})
        response.status_code = 400;
        return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
