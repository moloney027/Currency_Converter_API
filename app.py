from flask import Flask


def _initialize_error_handlers(application):
    from api.error_handler import errors
    application.register_blueprint(errors)


flaskAppInstance = Flask(__name__)

_initialize_error_handlers(flaskAppInstance)

if __name__ == '__main__':
    from api import *

    flaskAppInstance.run(debug=True, use_reloader=True)
