
from sqlalchemy import Column, Integer, String
from script import db

class Users(db.Model):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,autoincrement=True)   # id:int类型,是主键,自增
    name = Column(String(18),nullable=False,unique=True)    # 可以为空,唯一索引
    pwd = Column(String(18),nullable=False)






