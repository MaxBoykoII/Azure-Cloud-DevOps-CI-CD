import os

from flask import Flask


def create_app(script_info=None):
    app = Flask(__name__)

    config = AppConfig(app)
    config.configure()

    return app


class AppConfig:
    def __init__(self, app):
        self.app = app

    def configure(self):
        self.set_settings()
        self.set_blueprints()
        self.set_ctx()

    def set_settings(self):
        app_settings = os.getenv("APP_SETTINGS")
        self.app.config.from_object(app_settings)

    def set_blueprints(self):
        from src.api.ping import ping_blueprint
        from src.api.predict import predict_blueprint

        self.app.register_blueprint(ping_blueprint)
        self.app.register_blueprint(predict_blueprint)

    def set_ctx(self):
        app = self.app

        @app.shell_context_processor
        def ctx():
            return {"app": app}
