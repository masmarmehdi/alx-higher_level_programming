#!/usr/bin/python3
"""Linking a class to table in the database"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query_result = session.query(State).first()
    if not query_result:
        print("Nothing")
    else:
        print(query_result.id, query_result.name, sep=": ")
