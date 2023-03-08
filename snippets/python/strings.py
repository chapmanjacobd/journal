def split_multi(s, delimiters: list[str]):
    split_list = [s]
    for delimiter in delimiters:
        temp_list = []
        for s in split_list:
            temp_list.extend(s.split(delimiter))
        split_list = temp_list
    return split_list
