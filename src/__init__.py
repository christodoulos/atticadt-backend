from flask import Flask
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from mongoengine import connect


from os import environ, path
from dotenv import load_dotenv

from src.blueprints.atticadt import atticadt
from src.blueprints.attica_green import attica_green
from src.blueprints.apn_plc import apnplc
from src.blueprints.heatmap import heatmap

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

app = Flask(__name__)


connect(
    alias="attica_dt",
    db="attica_dt",
    host=environ.get("MONGODB_HOST"),
    port=int(environ.get("MONGODB_PORT")),
)
connect(
    alias="attica_green",
    db="attica_green",
    host=environ.get("MONGODB_HOST"),
    port=int(environ.get("MONGODB_PORT")),
)
connect(
    alias="impetus-dev",
    db="impetus-dev",
    host=environ.get("MONGODB_HOST"),
    port=int(environ.get("MONGODB_PORT")),
)


cors = CORS(
    app,
    resources={
        r"*": {"origins": ["http://localhost:4200", "https://atticadt.uwmh.eu"]}
    },
)


app.register_blueprint(atticadt, url_prefix="/atticadt")
app.register_blueprint(attica_green, url_prefix="/attica_green")
app.register_blueprint(apnplc, url_prefix="/apnplc")
app.register_blueprint(heatmap, url_prefix="/heatmap")

SWAGGER_URL = "/docs"
API_URL = "/static/swagger.json"

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "Test application"},
)

app.register_blueprint(swaggerui_blueprint)
