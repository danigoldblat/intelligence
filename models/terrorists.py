from sqlmodel import SQLModel, Field
from sqlmodel import create_engine
from sqlmodel import Session, select

class Terrorists(SQLModel,table=True):
    id:int=Field(default=None,primary_key=True)
    name:str