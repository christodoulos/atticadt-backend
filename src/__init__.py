from flask import Flask
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint


from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = [
    {
        "db": "attica_dt",
        "host": environ.get("MONGODB_HOST"),
        "port": int(environ.get("MONGODB_PORT")),
        "alias": "attica_dt",
    },
    {
        "db": "attica_green",
        "host": environ.get("MONGODB_HOST"),
        "port": int(environ.get("MONGODB_PORT")),
        "alias": "attica_green",
    },
    {
        "db": "impetus-dev",
        "host": environ.get("MONGODB_HOST"),
        "port": int(environ.get("MONGODB_PORT")),
        "alias": "impetus-dev",
    },
]

cors = CORS(
    app,
    resources={
        r"*": {"origins": ["http://localhost:4200", "https://atticadt.uwmh.eu"]}
    },
)

db = MongoEngine()
db.init_app(app)

from src.blueprints.atticadt import atticadt
from src.blueprints.attica_green import attica_green
from src.blueprints.apn_plc import apnplc
from src.blueprints.heatmap import heatmap

app.register_blueprint(atticadt, url_prefix="/atticadt")
app.register_blueprint(attica_green, url_prefix="/attica_green")
app.register_blueprint(apnplc, url_prefix="/apnplc")
app.register_blueprint(heatmap, url_prefix="/heatmap")

SWAGGER_URL = "/api/docs"  # URL for exposing Swagger UI (without trailing '/')
API_URL = "/static/swagger.json"  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        "app_name": "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)
