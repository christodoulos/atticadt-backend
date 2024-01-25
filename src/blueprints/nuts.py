from flask import Blueprint, Response
import json

from src.models.nuts import Nuts30

nuts = Blueprint("nuts", __name__)


@nuts.route("/<int:nut_level>", methods=["GET"])
def get_nuts(nut_level: int):
    nut_doc = Nuts30.objects(properties__LEVL_CODE=nut_level)

    return Response(
        response=nut_doc.to_json(),
        status=200,
        mimetype="application/json",
    )


@nuts.route("/<int:nut_level>/<string:nuts_id>", methods=["GET"])
def get_nuts_id(nut_level: int, nuts_id: str):
    print(nut_level, type(nut_level))
    nut_doc = (
        Nuts30.objects(properties__LEVL_CODE=nut_level, properties__NUTS_ID=nuts_id)
        .exclude("id")
        .first()
    )

    return Response(
        response=nut_doc.to_json(),
        status=200,
        mimetype="application/json",
    )
