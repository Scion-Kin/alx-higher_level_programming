#!/usr/bin/python3
'''This module defines a class named states for SQLAlchemy'''
from sqlalchemy import Integer, String, Column, MetaData
from sqlalchemy.ext.declarative import declarative_base

meta = MetaData()
Base = declarative_base()


class State(Base):
    ''' This defines a class named state '''

    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
