import mongoengine as me


class HipsBase(me.Document):
    date = me.DateTimeField(required=True)
    nuts_id = me.StringField(required=True)
    mean = me.FloatField(required=True)
    median = me.FloatField(required=True)
    min = me.FloatField(required=True)
    max = me.FloatField(required=True)

    meta = {"abstract": True, "indexes": ["date"]}


def HipsClassFactory(nuts_level, experiment, metric):
    class Hips(HipsBase):
        meta = {
            "collection": f"nuts_{nuts_level}:{experiment}:{metric}",
            "db_alias": "hips",
        }

    return Hips
