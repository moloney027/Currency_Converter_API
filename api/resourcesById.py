from flask_restful import Resource


class RESTResourceById(Resource):

    def post(self, identifier):
        return {"message": "Inside post method of RESTResourceById. ID = {}".format(identifier)}, 200

    def get(self, identifier):
        return {"message": "Inside get method of RESTResourceById. ID = {}".format(identifier)}, 200

    def put(self, identifier):
        return {"message": "Inside put method of RESTResourceById. ID = {}".format(identifier)}, 200

    def delete(self, identifier):
        return {"message": "Inside delete method of RESTResourceById. ID = {}".format(identifier)}, 200
