from src import db
import mongoengine as me


class APNPLC(db.Document):
    ts = me.DateTimeField(required=True)
    col3 = me.FloatField(required=True)
    col4 = me.FloatField(required=True)
    col5 = me.FloatField(required=True)
    col6 = me.FloatField(required=True)
    col7 = me.FloatField(required=True)
    col8 = me.FloatField(required=True)
    col9 = me.FloatField(required=True)
    col10 = me.FloatField(required=True)
    col11 = me.FloatField(required=True)

    meta = {"collection": "apn-plc", "db_alias": "impetus-dev"}
