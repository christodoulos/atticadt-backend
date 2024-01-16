import mongoengine as me
from src.models.shared import PointFeature


class HeatmapProperty(me.EmbeddedDocument):
    name = me.StringField(required=True, db_field="FeatureName")
    unit = me.StringField(required=True, db_field="FeatureUnit")
    obstime = me.StringField(required=True, db_field="TimeOfObservation")


class Heatmap(me.Document):
    type = me.StringField(required=True, default="FeatureCollection")
    properties = me.EmbeddedDocumentField(HeatmapProperty, required=True)
    name = me.StringField(required=True, unique=True)
    features = me.EmbeddedDocumentListField(PointFeature, required=True)
    meta = {"collection": "heatmaps", "db_alias": "attica_dt", "indexes": ["name"]}
