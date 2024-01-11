from flask import Flask
from flask_mongoengine import MongoEngine
from flask_cors import CORS

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

app.register_blueprint(atticadt, url_prefix="/atticadt")
app.register_blueprint(attica_green, url_prefix="/attica_green")
