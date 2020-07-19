from . import database
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import backref, relationship
from werkzeug.security import generate_password_hash, check_password_hash

class User(database.Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column("password", String(256), nullable=False)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self._password, password)


class Post(database.Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    created = Column(DateTime, default=func.now())
    title = Column(String)
    body = Column(String)