import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.ext.declarative import declarative_base
from zope.sqlalchemy import ZopeTransactionExtension
    
DBSession = orm.scoped_session(orm.sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class Group(Base):
    __tablename__ = "groups"
    query = DBSession.query_property()

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Unicode(255))
    short_name = sa.Column(sa.Unicode(32), index=True)

class Student(Base):
    __tablename__ = "students"
    query = DBSession.query_property()

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Unicode(255))
    grade = sa.Column(sa.Integer)
    group_id = sa.Column(sa.Integer, sa.ForeignKey("groups.id"))
    group = orm.relationship("Group", uselist=False, backref="students")
