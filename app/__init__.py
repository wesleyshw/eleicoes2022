from flask import Flask
from app import extensions

def create_app():
    app = Flask(__name__)
    extensions.init_app(app)

    from app.front.main import main as main_bp
    
    app.register_blueprint(main_bp)
    return app