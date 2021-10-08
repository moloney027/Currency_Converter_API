from flask_restful import Api
from app import flaskAppInstance
from .resources import CurrencyResource, ConverterResource

restServerInstance = Api(flaskAppInstance)

restServerInstance.add_resource(CurrencyResource, "/api/currency")
restServerInstance.add_resource(ConverterResource, "/api/currency/converter")
