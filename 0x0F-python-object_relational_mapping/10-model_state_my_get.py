#!/usr/bin/python3
"""List all stats from USE hbtn_0e_6_usa
"""
import sys
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Check for correct number of arguments
    if len(argv) != 5:
        print("Usage: {} username password database State".format(argv[0]))
        sys.exit(1)
    username, passwrd, dbname, stateName = sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, passwrd, dbname),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == stateName)\
        .first()
    # print the results
    if state is None:
        print("Not found")
    else:
        print("{}".format(state.id))
