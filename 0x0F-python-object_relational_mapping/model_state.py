#!/usr/bin/python3
'''This module defines a class named states for SQLAlchemy'''
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = column(Integer, unique=True, nullable=False, primary_key=True)
    name= column(String(128), nullable=False)
