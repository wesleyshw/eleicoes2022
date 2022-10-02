from flask_cors import CORS


def init_app(app):
    app.config["DEBUG"] = True
    CORS(app)

    @app.shell_context_processor
    def context_processor():

        return dict(app=app)