from src.config import DB_NAME
from datetime import datetime, timedelta
import mongoengine as me


class APNPLC(me.Document):
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
    col12 = me.FloatField(required=True)
    col13 = me.FloatField(required=True)
    col14 = me.FloatField(required=True)

    meta = {"collection": "apn-plc", "db_alias": DB_NAME}


    @staticmethod
    def get_last_records(days_limit: int):
        return APNPLC.objects(ts__gte=datetime.now() - timedelta(days=days_limit)).to_json()