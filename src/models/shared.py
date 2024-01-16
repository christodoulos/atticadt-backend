import mongoengine as me


class PointFeature(me.EmbeddedDocument):
    type = me.StringField(required=True, default="Feature")
    geometry = me.PointField(required=True)
    properties = me.DictField(required=True)


class PolygonFeature(me.EmbeddedDocument):
    type = me.StringField(required=True, default="Feature")
    geometry = me.PolygonField(required=True)
    properties = me.DictField(required=True)
    nuts_id = me.StringField(required=True, db_field="id")


class MultiPolygonFeature(me.EmbeddedDocument):
    type = me.StringField(required=True, default="Feature")
    geometry = me.MultiPolygonField(required=True)
    properties = me.DictField(required=True)
    nuts_id = me.StringField(required=True, db_field="id")
