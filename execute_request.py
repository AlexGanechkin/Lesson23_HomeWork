import os
from collections import Counter

from flask import abort

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
req = {
  "file_name": "apache_logs.txt",
  "cmd1": "limit",
  "value1": "20",
  "cmd2": "sort",
  "value2": "asc"
}

def load_file(filename: str):
    try:
        with open(f'{DATA_DIR}/{filename}') as f:
            while True:
                line = f.readline()
                if not line:
                    break
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
    #map(lambda lst, x: lst.append(x) if x not in lst else x, arr)
    return list(set(arr))


def _sort(arr: list, value: str):
    if value == 'asc':
        value = False
    else:
        value = True

    return list(sorted(arr, reverse=value))
