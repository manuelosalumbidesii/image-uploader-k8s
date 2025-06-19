from flask import Flask, request, jsonify, send_from_directory, abort
import os
from util import allowed_file, save_file, list_uploaded_files

UPLOAD_FOLDER = '/app/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = save_file(file, app.config['UPLOAD_FOLDER'])
        return jsonify({'message': 'File uploaded', 'filename': filename}), 201

    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/api/images', methods=['GET'])
def list_images():
    files = list_uploaded_files(app.config['UPLOAD_FOLDER'])
    return jsonify(files), 200

@app.route('/uploads/<filename>', methods=['GET'])
def serve_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/api/images/<filename>', methods=['DELETE'])
def delete_image(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return jsonify({'message': 'File deleted'}), 200
    else:
        return abort(404, description="File not found")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
