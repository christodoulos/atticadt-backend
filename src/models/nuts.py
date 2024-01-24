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


class Nuts30(me.Document):
    type = me.StringField(required=True, default="Feature")
    geometry = me.GenericEmbeddedDocumentField(
        choices=[me.PolygonField, me.MultiPolygonField]
    )
    # geometry = me.PolygonField(required=True)

    properties = me.DictField(required=True)
    nuts_id = me.StringField(required=True, db_field="id")

    meta = {"collection": "nuts30", "db_alias": "attica_dt"}
