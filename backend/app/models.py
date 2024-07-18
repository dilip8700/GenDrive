from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MediaSummary(db.Model):
    __tablename__ = 'media_summaries'
    id = db.Column(db.Integer, primary_key=True)
    media_type = db.Column(db.String(50))
    filename = db.Column(db.String(100))
    s3_url = db.Column(db.String(200))
    summary = db.Column(db.Text)

    def __init__(self, media_type, filename, s3_url, summary):
        self.media_type = media_type
        self.filename = filename
        self.s3_url = s3_url
        self.summary = summary

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
