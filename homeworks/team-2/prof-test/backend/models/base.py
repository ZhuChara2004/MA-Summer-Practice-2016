from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
 
engine = create_engine("postgresql://dima:12124343@localhost/proftest")
Base = declarative_base()
Base.metadata.create_all(engine)
Base.metadata.bind = engine
dbs = sessionmaker(bind=engine)
db = dbs()
