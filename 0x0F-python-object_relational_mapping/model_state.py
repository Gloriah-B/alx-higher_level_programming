#!/usr/bin/python3
"""Script to create a table in MySQL database and perform basic operations"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Main function."""
    # Check if three command-line arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Create the engine with MySQL connection string
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Insert a new state
    new_state = State(name='New State')
    session.add(new_state)
    session.commit()

    # Display all states
    states = session.query(State).all()
    for state in states:
        print(state.id, state.name)

    # Close the session
    session.close()


if __name__ == "__main__":
    main()
