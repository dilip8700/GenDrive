from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.database import init_db

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)
    
    init_db(app)
    
    from app.main.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from app.api.image import image as image_blueprint
    app.register_blueprint(image_blueprint, url_prefix='/api/image')
    
    from app.api.video import video as video_blueprint
    app.register_blueprint(video_blueprint, url_prefix='/api/video')
    
    # Comment out or remove the document blueprint registration
    # from app.api.document import document as document_blueprint
    # app.register_blueprint(document_blueprint, url_prefix='/api/document')

    return app
