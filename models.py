from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class Tasks(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    category = Column(String)
    task_name = Column(String)
    doer = Column(String)
    description = Column(String)
    date_end = Column(String)


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    user_role = Column(Integer)
    password = Column(String)


engine = create_engine("sqlite+pysqlite:///tasks.db", echo=True, future=True)
engine.connect()

Base.metadata.create_all(engine)

Session = sessionmaker(engine)
