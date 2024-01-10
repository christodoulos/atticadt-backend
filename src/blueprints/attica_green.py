from flask import Blueprint, Response, send_file
import pandas as pd
from io import BytesIO

from src.models.attica_green import Irrigation, IrrigationData, ClimaData

attica_green = Blueprint("attica_green", __name__)


@attica_green.route("/data", methods=["GET"])
def get_data():
    irrigation_headers = [
        "index",
        "timestamp",
        "start",
        "end",
        "conductivity_target",
        "ph_target",
        "conductivity",
        "ph",
        "disposal_time",
        "valve1_time",
        "valve2_time",
        "valve3_time",
        "valve4_time",
        "valve5_time",
        "valve6_time",
        "valve7_time",
        "valve8_time",
        "valve9_time",
        "valve10_time",
        "valve_fertilizer_a",
        "valve_fertilizer_b",
        "valve_fertilizer_c",
        "valve_fertilizer_d",
        "valve_fertilizer_e",
        "valve_fertilizer_f",
        "valve_fertilizer_g",
        "valve_fertilizer_h",
        "valve_fertilizer_i",
        "valve_fertilizer_j",
        "valve_fertilizer_acid",
        "empty",
    ]
    irrigation_data_headers = [
        "timestamp",
        "temperature_water",
        "conductivity_water",
        "ph_water",
        "temperature_runoff_1",
        "conductivity_runoff_1",
        "ph_runoff_1",
        "temperature_runoff_2",
        "conductivity_runoff_2",
        "ph_runoff_2",
        "sum_runoff_volume_1",
        "sum_runoff_volume_2",
        "sum_pump_time",
        "sum_waterings_volume_1",
        "sum_waterings_volume_2",
        "empty",
    ]
    clima_data_headers = [
        "timestamp",
        "temperature_out",
        "humidity_out",
        "sunshine",
        "temperature_1",
        "temperature_2",
        "humidity_1",
        "humidity_2",
        "is_raining",
        "windows_1",
        "windows_2",
        "empty_1",
        "empty_2",
        "empty_3",
        "empty_4",
        "empty_5",
    ]

    irrigation = Irrigation.objects().as_pymongo()
    irrigation_data = IrrigationData.objects().as_pymongo()
    clima_data = ClimaData.objects().as_pymongo()

    irrigation_df = pd.DataFrame(irrigation)[irrigation_headers]
    irrigation_data_df = pd.DataFrame(irrigation_data)[irrigation_data_headers]
    clima_data_df = pd.DataFrame(clima_data)[clima_data_headers]

    irrigation_df.sort_values(by="timestamp", ascending=False, inplace=True)
    irrigation_data_df.sort_values(by="timestamp", ascending=False, inplace=True)
    clima_data_df.sort_values(by="timestamp", ascending=False, inplace=True)

    output = BytesIO()
    writer = pd.ExcelWriter(output, engine="xlsxwriter")

    irrigation_df.to_excel(writer, sheet_name="irrigation")
    irrigation_data_df.to_excel(writer, sheet_name="irrigation_data")
    clima_data_df.to_excel(writer, sheet_name="clima_data")

    writer.close()
    output.seek(0)

    return Response(
        response=output.getvalue(),
        status=200,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-disposition": "attachment; filename=attica_green.xlsx"},
    )
