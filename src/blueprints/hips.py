from flask import Blueprint, Response
import json
from bson.json_util import dumps
from datetime import datetime

from src.models.hips import HipsFactory

from .utils import filter_results

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


@hips.route(
    "/<nuts_level>/<experiment>/<metric>/<from_date>/<to_date>", methods=["GET"]
)
def get_hips_date_range(nuts_level, experiment, metric, from_date, to_date):
    from_date = datetime.strptime(from_date, "%Y-%m-%d")
    to_date = datetime.strptime(to_date, "%Y-%m-%d")
    Hips = HipsFactory(nuts_level, experiment, metric)
    hips = Hips.objects(date__gte=from_date, date__lte=to_date).aggregate(
        {
            "$group": {
                "_id": "$nuts_id",
                "mean": {"$avg": "$mean"},
                "min": {"$min": "$min"},
                "max": {"$max": "$max"},
                "median": {"$avg": "$median"},
            }
        }
    )
    return Response(
        json.dumps(json.loads(dumps(hips))), mimetype="application/json", status=200
    )


@hips.route(
    "/<nuts_level>/<experiment>/<metric>/<from_date>/<to_date>/<nutid>", methods=["GET"]
)
def get_hips_date_range_nut(nuts_level, experiment, metric, from_date, to_date, nutid):
    from_date = datetime.strptime(from_date, "%Y-%m-%d")
    to_date = datetime.strptime(to_date, "%Y-%m-%d")
    Hips = HipsFactory(nuts_level, experiment, metric)
    hips = Hips.objects(
        date__gte=from_date, date__lte=to_date, nuts_id=nutid
    ).aggregate(
        {
            "$group": {
                "_id": "$nuts_id",
                "mean": {"$avg": "$mean"},
                "min": {"$min": "$min"},
                "max": {"$max": "$max"},
                "median": {"$avg": "$median"},
            }
        }
    )
    hips = list(hips)
    filter_results(list(hips), metric)
    return Response(json.dumps(hips), mimetype="application/json", status=200)
