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

    my_object = State(name="Louisiana")
    orm_session.add(my_object)
    orm_session.commit()

    print("{}".format(my_object.id))

    orm_session.close()
