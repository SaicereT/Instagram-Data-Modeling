import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Follower(Base):
    __tablename__ = 'follower'

    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey ('user.id'))
    user_from = relationship(User, lazy=False)
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user_to = relationship(User, lazy=False)

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey ('user.id'))
    user = relationship(User, lazy=True)

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    post_id = Column(Integer, ForeignKey ('post.id'))
    post = relationship (User, lazy=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    author = relationship(User ,lazy=True)

class Media(Base):
    __tablename__ = 'media'

    id = Column(Integer, primary_key=True)
    type = Column (Integer)
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey ('post.id'))
    post = relationship(Post, lazy=True)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
