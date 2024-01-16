import mongoengine as me
from src.models.shared import PolygonFeature, MultiPolygonFeature


class FeatureCollection(me.EmbeddedDocument):
    type = me.StringField(required=True, default="FeatureCollection")
    features = me.ListField(
        me.GenericEmbeddedDocumentField(choices=[PolygonFeature, MultiPolygonFeature]),
        required=True,
    )


class Nuts(me.Document):
    level = me.IntField(required=True, choices=[0, 1, 2, 3])
    scale = me.IntField(required=True, choices=[30])
    featureCollection = me.EmbeddedDocumentField(FeatureCollection, required=True)

    meta = {"collection": "nuts", "db_alias": "attica_dt"}
