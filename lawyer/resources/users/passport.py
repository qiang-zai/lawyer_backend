from flask_restful import Resource


class NewClientResource(Resource):
    def get(self):
        return {'name': 'zhangsan'}, 200


class AuthorizationResource(Resource):
    pass
