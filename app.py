from flask import Flask

flaskAppInstance = Flask(__name__)

if __name__ == '__main__':
    from api import *

    flaskAppInstance.run(debug=True, use_reloader=True)
