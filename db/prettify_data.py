from db import datetime_convert as dc

def raw_data_to_simple_table(raw_data):
    ret = []
    ret_line = []
    for line in raw_data.split("\n"):
        if len(line.split("\t")) == 1:
            ret_line.append(line)
        else:
            if ret_line != []:
                ret.append(ret_line)
            ret_line = line.split("\t")
    if ret_line != []:
        ret.append(ret_line)
    return ret


# Makes simple objects out of the table lines
def simple_table_to_prettified_table(simple_table):
    ret = []
    for line in simple_table:
        task = []
        task.append(line[0])
        task.append(dc.convert(line[1], "MM/DD/YY"))
        task.append(dc.convert(line[2], "HH:MM XM"))
        task.append(dc.convert(line[3], "HH:MM:SS"))
        task.append(dc.convert(line[4], "HH:MM:SS"))
        task.append(line[6])
        task.append(line[8])
        task.append(dc.convert(line[9], "HH:MM:SS"))
        ret.append(task)
    return ret


def raw_to_pretty_data(raw_data):
    data = raw_data_to_simple_table(raw_data)
    data = simple_table_to_prettified_table(data)
    return data
