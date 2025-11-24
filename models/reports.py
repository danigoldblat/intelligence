from sqlmodel import SQLModel, Field
from sqlmodel import create_engine
from sqlmodel import Session, select
from agents import Agents
from terrorists import Terrorists
import time

class Reports(SQLModel,table=True):
    Id:int=Field(default=None,primary_key=True)
    AgentsId:int=Field(default=None,foreign_key="Agents.id")
    TerroristsId:int=Field(default=None,foreign_key="terrorists.id")
    date:str
    category:str
    detail:str
engine=create_engine("mysql+mysqlconnector://root:@localhost/intelligence?use_pure=True") 