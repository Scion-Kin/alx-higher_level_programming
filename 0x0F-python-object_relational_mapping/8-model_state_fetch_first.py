#!/usr/bin/python3
'''This module executes an SQLAlchemy SQL search'''

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__" and len(sys.argv) == 4:
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).first()

    if (states):
        print("{}: {}".format(states.id, states.name))
    else: 
        print('Nothing')

    session.close()
