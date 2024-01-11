from flask import Blueprint, request, Response
import json

from src.models.apn_plc import APNPLC

apnplc = Blueprint("apnplc", __name__)


@apnplc.route("/<int:limit>", methods=["GET"])
def get_metrics(limit: int):
    metrics = APNPLC.objects[:limit].to_json()
    return Response(
        response=metrics,
        status=200,
        mimetype="application/json",
    )
