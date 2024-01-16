from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from mongoengine import connect


from src.blueprints.atticadt import atticadt
from src.blueprints.attica_green import attica_green
from src.blueprints.apn_plc import apnplc
from src.blueprints.heatmap import heatmap
from src.blueprints.hips import hips

SWAGGER_URL = "/docs"
API_URL = "/static/swagger.json"

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "Test application"},
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


app.register_blueprint(atticadt, url_prefix="/atticadt")
app.register_blueprint(attica_green, url_prefix="/attica_green")
app.register_blueprint(apnplc, url_prefix="/apnplc")
app.register_blueprint(heatmap, url_prefix="/heatmap")
app.register_blueprint(hips, url_prefix="/hips")


app.register_blueprint(swaggerui_blueprint)
