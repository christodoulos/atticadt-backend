from flask import Flask
from flask_cors import CORS
from mongoengine import connect
from src.config import *
from src.blueprints.apn_plc import apnplc
# from src.blueprints.atticadt import atticadt
# from src.blueprints.attica_green import attica_green
# from src.blueprints.heatmap import heatmap
# from src.blueprints.hips import hips
# from src.blueprints.nuts import nuts


app = Flask(__name__)


connect(alias=DB_NAME, db=DB_NAME, host=MONGO_HOST, port=MONGO_PORT)
# connect(alias="attica_green", db="attica_green", host=MONGO_HOST, port=MONGO_PORT)
# connect(alias="impetus-dev", db="impetus-dev", host=MONGO_HOST, port=MONGO_PORT)
# connect(alias="hips", db="hips", host=MONGO_HOST, port=MONGO_PORT)


cors = CORS(
    app,
    resources={
        r"*": {"origins": ["http://localhost:4200", "https://atticadt.ddns.net"]}
    },
)

app.register_blueprint(apnplc, url_prefix="/apnplc")
# app.register_blueprint(atticadt, url_prefix="/atticadt")
# app.register_blueprint(attica_green, url_prefix="/attica_green")
# app.register_blueprint(heatmap, url_prefix="/heatmap")
# app.register_blueprint(hips, url_prefix="/hips")
# app.register_blueprint(nuts, url_prefix="/nuts")
