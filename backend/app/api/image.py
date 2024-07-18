from flask import Blueprint, request, jsonify
import os
from app.utils.s3_utils import upload_file_to_s3
from app.utils.object_detection_image import detect_objects_in_image
from app.utils.image_summary import summarize_content_of_image

image = Blueprint('image', __name__)

@image.route('/detect-image-objects', methods=['POST'])
def detect_image_objects():
    """Endpoint to detect objects in an image."""
    if 'image' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    filepath = os.path.join('/tmp', file.filename)
    file.save(filepath)

    detected_objects = detect_objects_in_image(filepath)
    s3_url = upload_file_to_s3(filepath, s3_key=f"images/{file.filename}")
    os.remove(filepath)  # Clean up the uploaded file

    if detected_objects:
        return jsonify({"detected_objects": detected_objects, "s3_url": s3_url})
    else:
        return jsonify({"error": "Failed to detect objects"}), 500

@image.route('/summarize-image', methods=['POST'])
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
    s3_url = upload_file_to_s3(filepath, s3_key=f"images/{file.filename}")
    os.remove(filepath)  # Clean up the uploaded file

    if summarize_content:
        return jsonify({"summary": summarize_content, "s3_url": s3_url})
    else:
        return jsonify({"error": "Failed to create summary"}), 500
