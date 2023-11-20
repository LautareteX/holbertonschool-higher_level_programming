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

    states_a = orm_session.query(State).filter(State.name.like("%a%")).all()

    for i in states_a:
        orm_session.delete(i)
    orm_session.commit()

    orm_session.close()
