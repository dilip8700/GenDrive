from flask import Blueprint, request, jsonify
import os
from app.utils.s3_utils import upload_file_to_s3
from app.utils.video_summary import summarize_video
from app.models import MediaSummary

video = Blueprint('video', __name__)

@video.route('/summarize-video', methods=['POST'])
def summarize_video_endpoint():
    """Endpoint to summarize a video."""
    if 'video' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['video']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    filepath = os.path.join('/tmp', file.filename)
    file.save(filepath)

    try:
        summary = summarize_video(filepath)
        s3_url = upload_file_to_s3(filepath, s3_key=f"videos/{file.filename}")
    except Exception as e:
        os.remove(filepath)  # Clean up the uploaded file
        return jsonify({"error": str(e)}), 500

    os.remove(filepath)  # Clean up the uploaded file
    media_summary = MediaSummary('video', file.filename, s3_url, summary)
    media_summary.save_to_db()
    return jsonify({"summary": summary, "s3_url": s3_url})
