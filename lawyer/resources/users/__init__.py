from flask import Blueprint
from flask_restful import Api
from lawyer.resources.users import passport

# 1,创建蓝图对象
user_blue = Blueprint('user', __name__)
# 2,创建api对象,关联蓝图
user_api = Api(user_blue, catch_all_404s=True)
# 3,添加路由资源到api对象
user_api.add_resource(passport.NewClientResource, '/v1_0/new_client', endpoint='NewClient')

