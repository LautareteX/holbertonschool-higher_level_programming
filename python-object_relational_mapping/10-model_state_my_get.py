#!/usr/bin/python3
"""
No more beauty comments. I am very stressed.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    orm_session = Session()

    mg_object = orm_session.query(State).filter(
        State.name == sys.argv[4]).first()

    if mg_object:
        print("{}".format(mg_object.id))
    else:
        print("Not found")

    orm_session.close()
