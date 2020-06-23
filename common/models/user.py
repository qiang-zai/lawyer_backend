from common.models import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from common.models.expertise import db_lawyer_expertise


class TimeModel(object):
    ctime = db.Column('create_time', db.DateTime, default=datetime.now, doc='创建时间')
    utime = db.Column('update_time', db.DateTime, default=datetime.now, onupdate=datetime.now, doc='更新时间')


class User(db.Model, TimeModel):
    """
    用户基本信息
    """
    __tablename__ = 'user_basic'

    class STATUS:
        ENABLE = 1
        DISABLE = 0

    id = db.Column('user_id', db.Integer, primary_key=True, doc='用户ID')
    mobile = db.Column(db.String, doc='手机号')
    password_hash = db.Column('password', db.String(128), nullable=False)
    name = db.Column('user_name', db.String, doc='昵称、姓名')
    profile_photo = db.Column('user_photo', db.String, doc='头像')
    last_login = db.Column(db.DateTime, doc='最后登录时间')

    account = db.Column(db.String, doc='账号:做备用')
    status = db.Column(db.Integer, default=1, doc='状态，是否可用')
    company = db.Column('user_firm', db.String, doc='公司')
    position = db.Column('user_position', db.String, doc='公司职位')
    gender = db.Column('user_gender', db.Integer, default=0, doc='性别，0-男，1-女')
    city = db.Column('city_id', db.Integer, doc='所在城市')
    role = db.Column(db.Integer, default=1, doc='用户角色，0表示管理员，1表示普通用户，2表示律师用户')

    @property
    def password(self):
        raise AttributeError("当前属性不可读")

    @password.setter
    def password(self, value):
        self.password_hash = generate_password_hash(value)

    def check_passowrd(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "%s-%s" % (self.id, self.name)


class Lawyer(db.Model):
    """
    律师基本信息
    """
    __tablename__ = 'lawyer_basic'

    class STATUS:
        ENABLE = 1
        DISABLE = 0

    id = db.Column('lawyer_id', db.Integer, primary_key=True, doc='用户ID')
    real_name = db.Column(db.String, doc='律师用户姓名')
    practice_year = db.Column(db.Integer, doc='从业年限')
    lawyer_firm = db.Column('lawyer_firm', db.String, doc='律师事务所')
    is_certified = db.Column(db.Boolean, default=False, doc='是否认证，0表示未认证，1表示已认证')

    expert_ident = db.Column(db.String, doc='律师职业证号')
    profile = db.Column(db.String, doc='律师用户个人详细介绍')

    paid_for_once = db.Column(db.Integer, default=0, doc='单次咨询费用')
    paid_for_hour = db.Column(db.Integer, default=0, doc='每小时咨询付费')
    service_count = db.Column(db.Integer, default=0, doc='已经提供服务人数量')
    good_post_count = db.Column(db.Integer, default=0, doc='好评数量')
    mid_post_count = db.Column(db.Integer, default=0, doc='中评数量')
    bad_post_count = db.Column(db.Integer, default=0, doc='差评数量')
    all_post_count = db.Column(db.Integer, default=0, doc='所有评价数量')
    l_score = db.Column(db.DECIMAL(3, 2), default=0, doc='评分')

    expertises = db.relationship("Expertise", backref="lawyers", secondary=db_lawyer_expertise)


class Relation(db.Model, TimeModel):
    """
    用户关系表
    """
    __tablename__ = 'user_relation'

    class RELATION:
        DELETE = 0
        FOLLOW = 1
        BLACKLIST = 2

    id = db.Column('relation_id', db.Integer, primary_key=True, doc='主键ID')
    user_id = db.Column(db.Integer, db.ForeignKey('user_basic.user_id'), doc='普通用户ID')
    target_lawyer_id = db.Column(db.Integer, db.ForeignKey('user_basic.user_id'), doc='目标律师用户ID')
    relation = db.Column(db.Integer, doc='关系，0-取消，1-关注，2-拉黑')

    @staticmethod
    def is_following(user_id, lawyer_id):
        return Relation.query.filter_by(
            user_id=user_id,
            target_lawyer_id=lawyer_id,
            relation=Relation.RELATION.FOLLOW
        ).first()
