from flask import request, Blueprint, jsonify, make_response
from task.models import Task

bp = Blueprint('task', __name__)


@bp.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task().get_task(task_id)
    return make_response(jsonify(task), 200)


@bp.route('/', methods=['GET'])
def get_task_all():
    tasks = Task().get_all_tasks()
    return make_response(jsonify(tasks), 200)


@bp.route('/', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data.get('name'):
        return make_response(jsonify("Need name"), 400)
    if not data.get('status') and data.get('status') != 0:
        return make_response(jsonify("Need status"), 400)
    task = Task().add_task(data['name'], data.get("status"))
    return make_response(jsonify(task), 201)


@bp.route('/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    if not data.get('name'):
        return make_response(jsonify("Need name"), 400)
    if not data.get('status') and data.get('status') != 0:
        return make_response(jsonify("Need status"), 400)
    tasks = Task().update_task(task_id, **data)
    return make_response(jsonify(tasks), 200)


@bp.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    Task().delete_task(task_id)
    return make_response("Deleted successfully.", 200)
