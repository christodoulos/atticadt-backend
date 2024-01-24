import json
from src.models.nuts import *
import mongoengine as me

with open("NUTS_RG_03M_2021_4326.geojson") as json_file:
    data = json.load(json_file)
    for feature in data["features"]:
        print(feature["id"])
        if feature["geometry"]["type"] == "Polygon":
            geometry = MyPolygonField(
                coordinates=feature["geometry"]["coordinates"]
            )
        else: geometry = MyMultiPolygonField(coordinates=feature["geometry"]["coordinates"])

        new_nuts = Nuts30(
            type="Feature",
            geometry=geometry,
            properties=feature["properties"],
            nuts_id=feature["id"],
        )
        print(new_nuts)
        try:
            new_nuts.save()
        except me.ValidationError as e:
            print(e.to_dict())
            exit(1)
