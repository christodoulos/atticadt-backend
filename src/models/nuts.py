import mongoengine as me


class MyPolygonField(me.EmbeddedDocument):
    type = me.StringField(required=True, default="Polygon")
    coordinates = me.ListField(me.ListField(me.ListField(me.FloatField())))


class MyMultiPolygonField(me.EmbeddedDocument):
    type = me.StringField(required=True, default="MultiPolygon")
    coordinates = me.ListField(
        me.ListField(me.ListField(me.ListField(me.FloatField())))
    )


class Nuts30(me.Document):
    type = me.StringField(required=True, default="Feature")
    geometry = me.GenericEmbeddedDocumentField(
        choices=[MyPolygonField, MyMultiPolygonField]
    )

    properties = me.DictField(required=True)
    nuts_id = me.StringField(required=True)

    meta = {"collection": "nuts30", "db_alias": "attica_dt"}
