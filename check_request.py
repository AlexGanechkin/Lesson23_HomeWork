import re
from typing import Dict, Optional

from flask import abort


def get_request_data(data: Dict[str, str]) -> Dict[str, Optional[str]]:
    data_dict = {'file_name': data.get('file_name', None),
                 'cmd1': data.get('cmd1', None),
                 'value1': data.get('value1', None),
                 'cmd2': data.get('cmd2', None),
                 'value2': data.get('value2', None)
                 }

    check_filename(data_dict['file_name'])
    check_request(data_dict['cmd1'], data_dict['value1'])
    if data_dict['cmd2'] is not None:
        check_request(data_dict['cmd2'], data_dict['value2'])
    return data_dict


def check_filename(file_name: str) -> bool:
    pattern = '(^(.+)[^\.])\.txt$'
    if re.match(pattern, file_name) is None:
        abort(400)
    return True


def check_request(cmd: str, value: str) -> None:
    if cmd not in ('filter', 'limit', 'map', 'unique', 'sort', 'regex'):
        abort(400)

    if cmd == 'filter':
        if value == '' or value is None:
            abort(400)

    if cmd == 'limit':
        if not value.isdigit() or int(value) <= 0:
            abort(400)

    if cmd == 'map':
        if not value.isdigit() or int(value) < 0:
            abort(400)

    if cmd == 'sort':
        if value not in ('asc', 'desc'):
            abort(400)
