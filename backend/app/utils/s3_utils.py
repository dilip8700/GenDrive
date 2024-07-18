from app.config import Config

def upload_file_to_s3(file_path, s3_bucket=Config.S3_BUCKET, s3_key=None):
    """Uploads a file to an S3 bucket and returns the S3 URL."""
    if s3_key is None:
        s3_key = file_path.split('/')[-1]  # Use the file name as the S3 key if none provided
    try:
        Config.S3_CLIENT.upload_file(file_path, s3_bucket, s3_key)
        s3_url = f"https://{s3_bucket}.s3.{Config.S3_REGION}.amazonaws.com/{s3_key}"
        return s3_url
    except Exception as e:
        print(f"Error uploading to S3: {e}")
        return None
