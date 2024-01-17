from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from mongoengine import connect


from src.blueprints.atticadt import atticadt
from src.blueprints.attica_green import attica_green
from src.blueprints.apn_plc import apnplc
from src.blueprints.heatmap import heatmap
from src.blueprints.hips import hips
from src.blueprints.nuts import nuts

SWAGGER_URL = "/flask/docs"
API_URL = "/static/swagger.json"

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        "app_name": "Digital Twin of Attica API",
    },
)

app = Flask(__name__)


connect(alias="attica_dt", db="attica_dt")
connect(alias="attica_green", db="attica_green")
connect(alias="impetus-dev", db="impetus-dev")
connect(alias="hips", db="hips")


cors = CORS(
    app,
    resources={
        r"*": {"origins": ["http://localhost:4200", "https://atticadt.uwmh.eu"]}
    },
)


app.register_blueprint(atticadt, url_prefix="/flask/atticadt")
app.register_blueprint(attica_green, url_prefix="/flask/attica_green")
app.register_blueprint(apnplc, url_prefix="/flask/apnplc")
app.register_blueprint(heatmap, url_prefix="/flask/heatmap")
app.register_blueprint(hips, url_prefix="/flask/hips")
app.register_blueprint(nuts, url_prefix="/flask/nuts")


app.register_blueprint(swaggerui_blueprint)
