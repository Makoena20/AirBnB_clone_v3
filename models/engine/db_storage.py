#!/usr/bin/python3
"""This module defines the DBStorage engine."""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.base_model import BaseModel

class DBStorage:
    """This class manages the database storage."""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize the DBStorage instance."""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects of a particular class."""
        from models import classes
        query_objects = {}
        if cls:
            if isinstance(cls, str):
                cls = classes.get(cls, None)
            if cls:
                query_objects = self.__session.query(cls).all()
        else:
            for cl in classes.values():
                query_objects += self.__session.query(cl).all()
        return {type(obj).__name__ + '.' + obj.id: obj for obj in query_objects}

    def new(self, obj):
        """Add an object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session."""
        from models.base_model import Base
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """Close the current session."""
        self.__session.remove()

