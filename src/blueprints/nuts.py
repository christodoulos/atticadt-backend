from flask import Blueprint, Response
import json

from src.models.nuts import Nuts

nuts = Blueprint("nuts", __name__)


@nuts.route("/<int:nut_level>", methods=["GET"])
def get_nuts(nut_level: int):
    print(nut_level, type(nut_level))
    nut_doc = Nuts.objects(level=nut_level)

    return Response(
        response=nut_doc.to_json(),
        status=200,
        mimetype="application/json",
    )


@nuts.route("/<int:nut_level>/<string:nuts_id>", methods=["GET"])
def get_nuts_id(nut_level: int, nuts_id: str):
    print(nut_level, type(nut_level))
    nut_doc = list(Nuts.objects(level=nut_level))
    # print(nut_doc)

    for nut in nut_doc:
        wanted_feature = None
        for feature in nut.featureCollection.features:
            if feature.nuts_id == nuts_id:
                wanted_feature = feature
                break

    return Response(
        response=wanted_feature.to_json(),
        status=200,
        mimetype="application/json",
    )
