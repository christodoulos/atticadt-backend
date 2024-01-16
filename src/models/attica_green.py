import mongoengine as me


class Irrigation(me.Document):
    index = me.FloatField(required=True)
    timestamp = me.DateTimeField(required=True)
    start = me.FloatField(required=True)
    end = me.FloatField(required=True)
    conductivity_target = me.FloatField(required=True)
    ph_target = me.FloatField(required=True)
    conductivity = me.FloatField(required=True)
    ph = me.FloatField(required=True)
    disposal_time = me.FloatField(required=True)
    valve1_time = me.FloatField(required=True)
    valve2_time = me.FloatField(required=True)
    valve3_time = me.FloatField(required=True)
    valve4_time = me.FloatField(required=True)
    valve5_time = me.FloatField(required=True)
    valve6_time = me.FloatField(required=True)
    valve7_time = me.FloatField(required=True)
    valve8_time = me.FloatField(required=True)
    valve9_time = me.FloatField(required=True)
    valve10_time = me.FloatField(required=True)
    valve_fertilizer_a = me.FloatField(required=True)
    valve_fertilizer_b = me.FloatField(required=True)
    valve_fertilizer_c = me.FloatField(required=True)
    valve_fertilizer_d = me.FloatField(required=True)
    valve_fertilizer_e = me.FloatField(required=True)
    valve_fertilizer_f = me.FloatField(required=True)
    valve_fertilizer_g = me.FloatField(required=True)
    valve_fertilizer_h = me.FloatField(required=True)
    valve_fertilizer_i = me.FloatField(required=True)
    valve_fertilizer_j = me.FloatField(required=True)
    valve_fertilizer_acid = me.FloatField(required=True)
    empty = me.FloatField(required=True)

    meta = {"collection": "irrigation", "db_alias": "attica_green"}


class IrrigationData(me.Document):
    timestamp = me.DateTimeField(required=True)
    temperature_water = me.FloatField(required=True)
    conductivity_water = me.FloatField(required=True)
    ph_water = me.FloatField(required=True)
    temperature_runoff_1 = me.FloatField(required=True)
    conductivity_runoff_1 = me.FloatField(required=True)
    ph_runoff_1 = me.FloatField(required=True)
    temperature_runoff_2 = me.FloatField(required=True)
    conductivity_runoff_2 = me.FloatField(required=True)
    ph_runoff_2 = me.FloatField(required=True)
    sum_runoff_volume_1 = me.FloatField(required=True)
    sum_runoff_volume_2 = me.FloatField(required=True)
    sum_pump_time = me.FloatField(required=True)
    sum_waterings_volume_1 = me.FloatField(required=True)
    sum_waterings_volume_2 = me.FloatField(required=True)
    empty = me.FloatField(required=True)

    meta = {"collection": "irrigation_data", "db_alias": "attica_green"}


class ClimaData(me.Document):
    timestamp = me.DateTimeField(required=True)
    temperature_out = me.FloatField(required=True)
    humidity_out = me.FloatField(required=True)
    sunshine = me.FloatField(required=True)
    temperature_1 = me.FloatField(required=True)
    temperature_2 = me.FloatField(required=True)
    humidity_1 = me.FloatField(required=True)
    humidity_2 = me.FloatField(required=True)
    is_raining = me.FloatField(required=True)
    windows_1 = me.FloatField(required=True)
    windows_2 = me.FloatField(required=True)
    empty_1 = me.FloatField(required=True)
    empty_2 = me.FloatField(required=True)
    empty_3 = me.FloatField(required=True)
    empty_4 = me.FloatField(required=True)
    empty_5 = me.FloatField(required=True)

    meta = {"collection": "clima_data", "db_alias": "attica_green"}
