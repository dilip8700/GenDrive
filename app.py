from flask import Flask, request, jsonify
import os
from object_detection_image import detect_objects_in_image

app = Flask(__name__)

@app.route('/detect-objects', methods=['POST'])
def detect_image_objects_():
    """Endpoint to detect objects in an image."""
    if 'image' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    filepath = os.path.join('/tmp', file.filename)
    file.save(filepath)

    detected_objects = detect_objects_in_image(filepath)

    os.remove(filepath)  # Clean up the uploaded file

    if detected_objects:
        return jsonify(detected_objects)
    else:
        return jsonify({"error": "Failed to detect objects"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

