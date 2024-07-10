from flask import Flask, request, jsonify
import os
from images.object_detection_image import detect_objects_in_image
from images.image_summary import summarize_content_of_image
app = Flask(__name__)

@app.route('/detect-image-objects', methods=['POST'])
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

@app.route('/summarize-image', methods=['POST'])
def summarize_image_content():
    """Endpoint to Create Summary of an image."""
    if 'image' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    filepath = os.path.join('/tmp', file.filename)
    file.save(filepath)

    summarize_content = summarize_content_of_image(filepath)

    os.remove(filepath)  # Clean up the uploaded file

    if summarize_content:
        return jsonify(summarize_content)
    else:
        return jsonify({"error": "Failed to create summary"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
