#!/usr/bin/python3
"""Defines the Base model."""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class BaseModel:
    """A base class for all models"""
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

