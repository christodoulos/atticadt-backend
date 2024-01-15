# from src import db
import mongoengine as me


class Point(me.EmbeddedDocument):
    lng = me.FloatField(min_value=-180, max_value=180)
    lat = me.FloatField(min_value=-90, max_value=90)


class Scale(me.EmbeddedDocument):
    x = me.FloatField(min_value=0)
    y = me.FloatField(min_value=0)
    z = me.FloatField(min_value=0)


class Rotation(me.EmbeddedDocument):
    x = me.FloatField(min_value=0)
    y = me.FloatField(min_value=0)
    z = me.FloatField(min_value=0)


class GLBModel(me.EmbeddedDocument):
    name = me.StringField(required=True, db_field="id")
    where = me.EmbeddedDocumentField(Point, required=True)
    elevation = me.FloatField(min_value=0, required=True)
    glb = me.StringField(required=True)
    scale = me.EmbeddedDocumentField(Scale, required=True)
    rotation = me.EmbeddedDocumentField(Rotation, required=True)
    castShadow = me.BooleanField(required=True)
    tooltip = me.StringField(required=True)


class Location(me.Document):
    name = me.StringField(required=True)
    center = me.EmbeddedDocumentField(Point, required=True)
    zoom = me.FloatField(min_value=0, max_value=20)
    bearing = me.FloatField(min_value=0, max_value=360)
    pitch = me.FloatField(min_value=0, max_value=60)
    glbModels = me.EmbeddedDocumentListField(GLBModel)

    meta = {"collection": "locations", "db_alias": "attica_dt"}
