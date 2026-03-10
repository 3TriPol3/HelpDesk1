from tkinter.constants import CASCADE

from Models.Category import Category
from Models.Base import *
from Models.User import User

class KnowledgeBase(BaseModel):
    id = PrimaryKeyField()