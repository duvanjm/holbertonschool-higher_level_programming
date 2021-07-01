#!/usr/bin/python3
"""module"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, engine
from model_city import City, Base
from model_state import Base, State
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    quer = session.query(City, State).join(State, State.id == City.state_id)\
        .order_by(City.id.asc()).all()
    for city in quer:
        print('{}: ({}) {}'.format(city.State.name,
                                   city.City.id,
                                   city.City.name))
    session.close()
