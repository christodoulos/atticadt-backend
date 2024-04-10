from sshtunnel import SSHTunnelForwarder
from datetime import datetime, timedelta
import time
import requests
from pymongo import MongoClient
from pprint import pprint

with SSHTunnelForwarder(
    ("atticadt.uwmh.eu", 22),
    ssh_username="atticadt",
    ssh_pkey="../.ssh/idrsa.pub",
    remote_bind_address=("localhost", 27017),
    local_bind_address=("localhost", 27027),
) as tunnel:
    print("Tunnel established on local 27027 to remote 27017")

    client = MongoClient("mongodb://localhost:27027/")
    db = client["attica_green"]
    irrigation = db["irrigation"]
    irrigation_data = db["irrigation_data"]
    clima_data = db["clima_data"]

    REPORTS_URL = "http://hcw0833nsrx.sn.mynetname.net:37646/SD/REPORTS"
    DATA_URL = "http://hcw0833nsrx.sn.mynetname.net:37646/SD/DATA"
    CLIMA_URL = "http://hcw0833nsrx.sn.mynetname.net:37647/SD/DATA"

    def url_suffix(date: datetime, prefix: str):
        year = date.year
        month = date.month
        if month < 10:
            month = f"0{month}"
        date_str = date.strftime("%d%m%y")
        if prefix != "RE":
            prefix = "D"
        return f"/{month}_{year}/{prefix}{date_str}.TXT"

    def correct_date_format(date_string):
        try:
            date_object = datetime.strptime(date_string, "%H:%M:%S %d/%m/%Y")
        except ValueError:
            time_string, date_string = date_string.split(" ")
            hours, minutes, seconds = map(int, time_string.split(":"))
            if minutes == 60:
                hours += 1
                minutes = 0
            if hours == 24:
                hours = 0
                date_object = datetime.strptime(date_string, "%d/%m/%Y") + timedelta(
                    days=1
                )
                date_string = date_object.strftime("%d/%m/%Y")
            corrected_date_string = (
                f"{hours:02d}:{minutes:02d}:{seconds:02d} {date_string}"
            )
            return corrected_date_string
        else:
            return date_string

    def document(data: str, prefix: str):
        alist = data.split(";")
        if prefix == "RE":
            index = int(alist[0])
            timestamp = datetime.strptime(alist[1], "%H:%M:%S %d/%m/%Y")
            start = int(alist[2])
            end = int(alist[3])
            conductivity_target = float(alist[4])
            ph_target = float(alist[5])
            conductivity = float(alist[6])
            ph = float(alist[7])
            disposal_time = float(alist[8])
            valve1_time = float(alist[9])
            valve2_time = float(alist[10])
            valve3_time = float(alist[11])
            valve4_time = float(alist[12])
            valve5_time = float(alist[13])
            valve6_time = float(alist[14])
            valve7_time = float(alist[15])
            valve8_time = float(alist[16])
            valve9_time = float(alist[17])
            valve10_time = float(alist[18])
            valve_fertilizer_a = float(alist[19])
            valve_fertilizer_b = float(alist[20])
            valve_fertilizer_c = float(alist[21])
            valve_fertilizer_d = float(alist[22])
            valve_fertilizer_e = float(alist[23])
            valve_fertilizer_f = float(alist[24])
            valve_fertilizer_g = float(alist[25])
            valve_fertilizer_h = float(alist[26])
            valve_fertilizer_i = float(alist[27])
            valve_fertilizer_j = float(alist[28])
            valve_fertilizer_acid = float(alist[29])
            empty = float(alist[30].strip())

            return {
                "_id": timestamp,
                "index": index,
                "timestamp": timestamp,
                "start": start,
                "end": end,
                "conductivity_target": conductivity_target,
                "ph_target": ph_target,
                "conductivity": conductivity,
                "ph": ph,
                "disposal_time": disposal_time,
                "valve1_time": valve1_time,
                "valve2_time": valve2_time,
                "valve3_time": valve3_time,
                "valve4_time": valve4_time,
                "valve5_time": valve5_time,
                "valve6_time": valve6_time,
                "valve7_time": valve7_time,
                "valve8_time": valve8_time,
                "valve9_time": valve9_time,
                "valve10_time": valve10_time,
                "valve_fertilizer_a": valve_fertilizer_a,
                "valve_fertilizer_b": valve_fertilizer_b,
                "valve_fertilizer_c": valve_fertilizer_c,
                "valve_fertilizer_d": valve_fertilizer_d,
                "valve_fertilizer_e": valve_fertilizer_e,
                "valve_fertilizer_f": valve_fertilizer_f,
                "valve_fertilizer_g": valve_fertilizer_g,
                "valve_fertilizer_h": valve_fertilizer_h,
                "valve_fertilizer_i": valve_fertilizer_i,
                "valve_fertilizer_j": valve_fertilizer_j,
                "valve_fertilizer_acid": valve_fertilizer_acid,
                "empty": empty,
            }
        elif prefix == "D":
            timestamp = datetime.strptime(
                correct_date_format(alist[0]), "%H:%M:%S %d/%m/%Y"
            )
            temperature_water = float(alist[1])
            conductivity_water = float(alist[2])
            ph_water = float(alist[3])
            temperature_runoff_1 = float(alist[4])
            conductivity_runoff_1 = float(alist[5])
            ph_runoff_1 = float(alist[6])
            temperature_runoff_2 = float(alist[7])
            conductivity_runoff_2 = float(alist[8])
            ph_runoff_2 = float(alist[9])
            sunmeter_below_2 = float(alist[10])
            humidity_substrate_place_2 = float(alist[11])
            humidity_substrate_1_place_1 = float(alist[12])
            humidity_substrate_2_place_1 = float(alist[13])
            sunmeter_below_1 = float(alist[14])
            co2_1 = float(alist[15].strip())

            return {
                "_id": timestamp,
                "timestamp": timestamp,
                "temperature_water": temperature_water,
                "conductivity_water": conductivity_water,
                "ph_water": ph_water,
                "temperature_runoff_1": temperature_runoff_1,
                "conductivity_runoff_1": conductivity_runoff_1,
                "ph_runoff_1": ph_runoff_1,
                "temperature_runoff_2": temperature_runoff_2,
                "conductivity_runoff_2": conductivity_runoff_2,
                "ph_runoff_2": ph_runoff_2,
                "sunmeter_below_2": sunmeter_below_2,
                "humidity_substrate_place_2": humidity_substrate_place_2,
                "humidity_substrate_1_place_1": humidity_substrate_1_place_1,
                "humidity_substrate_2_place_1": humidity_substrate_2_place_1,
                "sunmeter_below_1": sunmeter_below_1,
                "co2_1": co2_1,
            }
        else:
            timestamp = datetime.strptime(
                correct_date_format(alist[0]), "%H:%M:%S %d/%m/%Y"
            )
            temperature_out = float(alist[1])
            humidity_out = float(alist[2])
            sunshine = float(alist[3])
            temperature_1 = float(alist[4])
            temperature_2 = float(alist[5])
            humidity_1 = float(alist[6])
            humidity_2 = float(alist[7])
            is_raining = int(float(alist[8]))
            windows_1 = float(alist[9])
            windows_2 = float(alist[10])
            sunmeter_above_2 = float(alist[11])
            curtain_1 = float(alist[12])
            curtain_2 = float(alist[13])
            fan_1 = float(alist[14])
            fan_2 = float(alist[15].strip())

            return {
                "_id": timestamp,
                "timestamp": timestamp,
                "temperature_out": temperature_out,
                "humidity_out": humidity_out,
                "sunshine": sunshine,
                "temperature_1": temperature_1,
                "temperature_2": temperature_2,
                "humidity_1": humidity_1,
                "humidity_2": humidity_2,
                "is_raining": is_raining,
                "windows_1": windows_1,
                "windows_2": windows_2,
                "sunmeter_above_2": sunmeter_above_2,
                "curtain_1": curtain_1,
                "curtain_2": curtain_2,
                "fan_1": fan_1,
                "fan_2": fan_2,
            }

    def get_data(date: datetime, suffix_chars: str):
        documents = []
        suffix = url_suffix(date, suffix_chars)
        if suffix_chars == "RE":
            url = REPORTS_URL + suffix
        elif suffix_chars == "D":
            url = DATA_URL + suffix
        else:
            url = CLIMA_URL + suffix

        print(url)

        max_trials = 5
        data_received = False
        for index in range(max_trials):
            try:
                response = requests.get(url, timeout=30)
                data_received = True
                break
            except Exception as e:
                print("broken")
                time.sleep(5)

        if not data_received:
            return []

        for line in response.text.split("\n"):
            if line:
                documents.append(document(line, suffix_chars))

        return documents

    attica_green = [("RE", irrigation), ("D", irrigation_data), ("CLIMA", clima_data)]
    # attica_green = [("CLIMA", clima_data )]

    # for days in range(7):
    for suffix_chars, collection in attica_green:
        print(suffix_chars)
        # data = get_data(datetime.now() - timedelta(days=days), suffix_chars)
        data = get_data(datetime.now(), suffix_chars)
        for line in data:
            pprint(line)
            print(line["_id"])
            collection.update_one({"_id": line["_id"]}, {"$set": line}, upsert=True)
