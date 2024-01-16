from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.debug = True

    from .views import main_views, upload_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(upload_views.bp)
    return app
