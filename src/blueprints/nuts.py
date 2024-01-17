from flask import Blueprint, Response
import json

from src.models.nuts import Nuts

nuts = Blueprint("nuts", __name__)


@nuts.route("/<int:nut_level>", methods=["GET"])
def get_nuts(nut_level: int):
    print(nut_level, type(nut_level))
    nut_doc = Nuts.objects.filter(level=nut_level)

    return Response(
        response=nut_doc.to_json(),
        status=200,
        mimetype="application/json",
    )
