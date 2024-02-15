from flask import Flask
from .route.football import football
from .route.cricket import cricket

app = Flask(__name__, instance_relative_config=True)

def create_app():
    app.config.from_object('config.default')
    app.config.from_envvar('APP_CONFIG_FILE')
    app.config.from_pyfile('config.py')
    

    app.register_blueprint(football, url_prefix= "/football")
    app.register_blueprint(cricket, url_prefix= "/cricket")

    print(app.config['DEBUG'])

    @app.route('/home', methods = ["GET", "POST"])
    def index():
        print(app.config['DEBUG'])
        return app.config['DEBUG']
    
    return app
