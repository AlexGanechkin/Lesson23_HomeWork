from typing import Any, Dict, Callable

from flask import Blueprint, request, jsonify, Response

from check_request import get_request_data
from execute_request import load_file, _filter, _limit, _map, _unique, _sort, _regex

functions: Dict[str, Callable] = {'filter': _filter,
             'limit': _limit,
             'map': _map,
             'unique': _unique,
             'sort': _sort,
             'regex': _regex
             }

query_blueprint = Blueprint('perform_query', __name__)


@query_blueprint.route("/perform_query", methods=['POST'])
def perform_query() -> Response:
    data = request.json
    data_dict: Dict[str, str] = get_request_data(data)
    lines = load_file(data_dict['file_name'])

    response = functions[data_dict['cmd1']](lines, data_dict['value1'])
    if data_dict['cmd2'] is not None:
        response = functions[data_dict['cmd2']](response, data_dict['value2'])
    return jsonify(response)
