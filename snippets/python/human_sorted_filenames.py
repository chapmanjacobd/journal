#!/usr/bin/python3
# SPDX-License-Identifier: WTFPL

import locale
import pathlib
import re


def extract_ints(line):
    # split the string into parts:
    # - string with digits are coerced to int and thus compared as ints
    # - non-digits are compared as string

    # since we then rely in python's standard comparison operators
    # a str cannot be compared to an int...
    # so we prepend a type id that makes only compatible types are compared
    # `(type_id, real_value)`
    # - 0 if int
    # - 1 if str
    # when 2 type_id are different, python will sort them apart
    # without considering the real_value to compare

    ret = []
    for part_str in re.findall(r"\D+|\d+", line):
        try:
            part_as_num = int(part_str)
        except ValueError:
            # not a number, keep as is
            ret.append((1, part_str))
        else:
            ret.append((0, part_as_num))

    return tuple(ret)


def collate_strs(tup):
    return tuple(
        (type, part)
        if type == 0
        else (type, locale.strxfrm(part.rstrip("\x00")))
        for type, part in tup
    )


def file_key(path):
    return collate_strs(extract_ints(path.name))


locale.setlocale(locale.LC_ALL, "")

files = pathlib.Path().iterdir()
files = sorted(files, key=file_key)
print(*files, sep="\n")
