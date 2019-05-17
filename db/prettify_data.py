

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



def raw_to_pretty_data(raw_data):
    simple_table = raw_data_to_simple_table(raw_data)
    return simple_table
