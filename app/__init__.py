from flask import Flask

def create_app():
    app = Flask(__name__) # flask application instance

    from .routes import main     # Import the blueprint for routing

    app.register_blueprint(main)  #  Register the blueprint to bind routes 

    return app