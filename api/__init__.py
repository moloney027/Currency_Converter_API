from flask_restful import Api
from app import flaskAppInstance
from .resources import RESTResource
from .resourcesById import RESTResourceById


restServerInstance = Api(flaskAppInstance)

restServerInstance.add_resource(RESTResource, "/api")
restServerInstance.add_resource(RESTResourceById, "/api/id/<string:identifier>")
