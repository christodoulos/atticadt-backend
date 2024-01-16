from flask import Blueprint, Response
import json
from datetime import datetime

from src.models.hips import HipsFactory

hips = Blueprint("hips", __name__)


@hips.route("/<nuts_level>/<experiment>/<metric>", methods=["GET"])
def get_hips(nuts_level, experiment, metric):
    Hips = HipsFactory(nuts_level, experiment, metric)
    hips = Hips.objects().first().to_json()
    return Response(hips, mimetype="application/json", status=200)


@hips.route("/<nuts_level>/<experiment>/<metric>/<date>", methods=["GET"])
def get_hips_date(nuts_level, experiment, metric, date):
    date = datetime.strptime(date, "%Y-%m-%d")
    Hips = HipsFactory(nuts_level, experiment, metric)
    hips = Hips.objects(date=date).to_json()
    return Response(hips, mimetype="application/json", status=200)
