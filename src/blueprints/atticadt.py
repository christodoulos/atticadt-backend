from flask import Blueprint, request, Response
import json

from src.models.location import Location

atticadt = Blueprint("atticadt", __name__)


@atticadt.route("/locations", methods=["GET"])
def get_locations():
    locations = Location.objects().to_json()
    return Response(
        response=locations,
        status=200,
        mimetype="application/json",
    )


@atticadt.route("/locations", methods=["POST"])
def post_location():
    try:
        location = Location(**request.json).save()
    except Exception as e:
        error = {"error": str(e)}
        return Response(
            response=json.dumps(error),
            mimetype="application/json",
            status=400,
        )
    return Response(
        response=location,
        status=201,
    )


@atticadt.route("/locations/<name>", methods=["GET"])
def get_location(name: str):
    location = Location.objects(name=name)
    if not location:
        return Response(
            response=json.dumps({"error": "Location not found"}),
            status=404,
            mimetype="application/json",
        )
    else:
        return Response(
            response=location[0].to_json(),
            status=200,
            mimetype="application/json",
        )
