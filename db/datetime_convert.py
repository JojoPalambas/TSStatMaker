import datetime

def convert(value, format):
    if format == "MM/DD/YY":
        split_value = value.split("/")
        return datetime.date(2000 + int(split_value[2]), int(split_value[0]), int(split_value[1]))
    if format == "HH:MM XM":
        split_value = value.split(" ")
        hm = split_value[0].split(":")
        if split_value[1] == "AM":
            return datetime.time(int(hm[0]), int(hm[1]), 0)
        return datetime.time((int(hm[0]) + 12) % 24, int(hm[1]), 0)
    if format == "HH:MM:SS":
        split_value = value.split(":")
        return datetime.timedelta(hours=int(split_value[0]), minutes=int(split_value[1]), seconds=int(split_value[2]))
    return None
