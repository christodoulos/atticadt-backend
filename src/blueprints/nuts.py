from flask import Blueprint, request, Response
import json

from src.models.nuts import Nuts

nuts = Blueprint("nuts", __name__)


@nuts.route("/<int:nut_level>", methods=["GET"])
def get_nuts(nut_level: int):
    print(nut_level, type(nut_level))
    nnuts = Nuts.objects.filter(level=nut_level)

    # if not nnuts:
    #     return Response(
    #         response=json.dumps({"error": "Nuts not found"}),
    #         status=404,
    #         mimetype="application/json",
    #     )
    # else:
    #     return Response(
    #         response=nnuts.to_json(),
    #         status=200,
    #         mimetype="application/json",
    #     )
    return Response(
        response=nnuts.to_json(),
        status=200,
        mimetype="application/json",
    )
