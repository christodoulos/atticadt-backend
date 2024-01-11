import mongoengine as me


class PointFeature(me.EmbeddedDocument):
    type = me.StringField(required=True, default="Feature")
    geometry = me.PointField(required=True)
    properties = me.DictField(required=True)
