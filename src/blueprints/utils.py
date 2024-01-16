def filter_results(alist, metric):
    if "temperature" in metric:
        for item in alist:
            item["mean"] = item["mean"] - 273.15
            item["min"] = item["min"] - 273.15
            item["max"] = item["max"] - 273.15
            item["median"] = item["median"] - 273.15
