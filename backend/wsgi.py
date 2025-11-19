from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")


    @app.route("/")
    def home():
        return "What did the Dordt say when asked if they wanted memes? Yes, we 'dort'!"
    # initialize extensions
    #db.init_app(app)

    # register blueprints
    #from .routes import bp
    #app.register_blueprint(bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=False)
