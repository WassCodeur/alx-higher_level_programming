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
    if len(argv) != 4:
        print("Usage: {} username password database".format(argv[0]))
        sys.exit(1)
    username, passwrd, dbname = sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, passwrd, dbname),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id.asc()).first()
    # print the results
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
