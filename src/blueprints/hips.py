from flask import Blueprint, request, Response
import json

from src.models.hips import HipsFactory

hips = Blueprint("hips", __name__)


@hips.route("/<string:nuts_level>/<string:experiment>/<string:metric>", methods=["GET"])
def get_hips(nuts_level, experiment, metric):
    Hips = HipsFactory(nuts_level, experiment, metric)
    hips = Hips.objects().first().to_json()
    return Response(hips, mimetype="application/json", status=200)
