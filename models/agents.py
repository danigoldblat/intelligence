from sqlmodel import SQLModel, Field
from sqlmodel import create_engine
from sqlmodel import Session, select
class Agents(SQLModel,table=True):
    id:int=Field(default=None,primary_key=True)
    name:str
    password:str=Field(unique=True)
engine=create_engine("mysql+mysqlconnector://root:@localhost/intelligence?use_pure=True")    
