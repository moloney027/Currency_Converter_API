from flask import Blueprint, jsonify
from werkzeug.exceptions import HTTPException

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(Exception)
def handle_error(e):
    # Handle HTTPExceptions
    if isinstance(e, HTTPException):
        return jsonify({'message': e.description}), e.code
    status_code = 500
    response = {
        'error': {'message': str(e)}}
    return jsonify(response), status_code
