from common.models import db


class Expertise(db.Model):
    """
    专业
    """
    __tablename__ = 'expertise'

    id = db.Column('expertise_id', db.Integer, primary_key=True, doc='专业ID')
    name = db.Column('expertise_name', db.String, doc='专业名字')


db_lawyer_expertise = db.Table(
    "lawyer_expertise",
    db.Column("lawyer_id", db.Integer, db.ForeignKey("lawyer_basic.lawyer_id")),
    db.Column("expertise_id", db.Integer, db.ForeignKey("expertise.expertise_id"))
)
