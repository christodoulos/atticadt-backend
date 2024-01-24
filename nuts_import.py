import json
from src.models.nuts import Nuts30
from src.models.shared import PolygonFeature, MultiPolygonFeature
from pprint import pprint
import mongoengine as me

with open("NUTS_RG_03M_2021_4326.geojson") as json_file:
    data = json.load(json_file)
    for feature in data["features"]:
        # print(feature)
        # if feature["geometry"]["type"] == "Polygon":
        #     geometry = me.PolygonField(
        #         type="Polygon", coordinates=feature["geometry"]["coordinates"]
        #     )
        # else:
        #     geometry = me.MultiPolygonField(
        #         type="MultiPolygon", coordinates=feature["geometry"]["coordinates"]
        #     )
        # print(geometry)
        # new_nuts = Nuts30(
        #     type="Feature",
        #     geometry=geometry,
        #     properties=feature["properties"],
        #     nuts_id=feature["id"],
        # )
        feature["nuts_id"] = feature["id"]
        feature.pop("id")
        new_nuts = Nuts30(**feature)
        # new_nuts.save()
        try:
            new_nuts.save()
        except me.ValidationError as e:
            print(e.to_dict())
