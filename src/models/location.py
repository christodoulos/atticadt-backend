from src import db
import mongoengine as me


class Center(me.EmbeddedDocument):
    lng = me.FloatField(min_value=-180, max_value=180)
    lat = me.FloatField(min_value=-90, max_value=90)


class Location(db.Document):
    name = me.StringField(required=True)
    center = me.EmbeddedDocumentField(Center, required=True)
    zoom = me.FloatField(min_value=0, max_value=20)
    bearing = me.FloatField(min_value=0, max_value=360)
    pitch = me.FloatField(min_value=0, max_value=60)

    meta = {"collection": "locations", "db_alias": "attica_dt"}
