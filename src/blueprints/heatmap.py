from flask import Blueprint, request, Response
import json

from src.models.heatmap import Heatmap

heatmap = Blueprint("heatmap", __name__)


@heatmap.route("/<string:name>", methods=["GET"])
def get_heatmap(name: str):
    heatmap = Heatmap.objects.filter(name=name)
    if not heatmap:
        return Response(
            response=json.dumps({"error": "Heatmap not found"}),
            status=404,
            mimetype="application/json",
        )
    else:
        return Response(
            response=heatmap[0].to_json(),
            status=200,
            mimetype="application/json",
        )


@heatmap.route("/<string:name>", methods=["POST"])
def post_heatmap(name: str):
    h = Heatmap.objects(name=name)
    if len(h) == 1:
        h_id = h[0].id
        heatmap = Heatmap(**request.json, id=h_id).save()
        return Response(
            response=heatmap.to_json(),
            status=200,
            mimetype="application/json",
        )
    else:
        error = {"error": f"Heatmap with name {name} not found"}
        return Response(
            response=json.dumps(error),
            mimetype="application/json",
            status=404,
        )
