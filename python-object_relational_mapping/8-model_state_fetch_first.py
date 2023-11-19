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

    first_st = orm_session.query(State).first()

    if first_st:
        print("{}: {}".format(first_st.id, first_st.name))
    else:
        print("Nothing")

    orm_session.close()
