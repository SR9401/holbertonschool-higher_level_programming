#!/usr/bin/python3
"""
sssss
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    ssss
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username,
                                                         password, db_name),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    s = session.query(State).filter(State.name.like('%a%')).all()
    for state in s:
        session.delete(state)
    session.commit()
