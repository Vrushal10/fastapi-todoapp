from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import URL

# SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

SQLALCHEMY_DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password="Krishna@1234",
    host="localhost",
    port=5432,
    database="TodoApplicationDB",
)

# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()

