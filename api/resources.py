from flask_restful import Resource


class RESTResource(Resource):

    def post(self):
        return {"message": "Inside post method"}, 200

    def get(self):
        return {"message": "Inside get method"}, 200

    def put(self):
        return {"message": "Inside put method"}, 200

    def delete(self):
        return {"message": "Inside delete method"}, 200
