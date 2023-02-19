import os
import re

from flask import abort

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


def load_file(filename: str):
    try:
        with open(f'{DATA_DIR}/{filename}') as f:
            for line in f:
                yield line
    except FileNotFoundError:
        abort(400)


def _filter(arr: list, value: str):
    return list(filter(lambda x: value in x, arr))


def _limit(arr: list, value: str):
    return list(arr)[:int(value)]


def _map(arr: list, value: int):
    response = map(lambda x: x.split(' '), arr)
    column_select = map(lambda x: x[int(value)], response)
    return list(column_select)


def _unique(arr: list, value):
    unique_list = []
    for item in arr:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


def _sort(arr: list, value: str):
    if value == 'asc':
        value = False
    else:
        value = True

    return list(sorted(arr, reverse=value))


def _regex(arr: list, value: str):
    pattern = re.compile(value)
    return list(filter(lambda x: bool(pattern.findall(x)), arr))
