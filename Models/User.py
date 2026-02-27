from Models.Base import *

class User(BaseModel):
    id = PrimaryKeyField()
    login = CharField(unique=True, max_length=10)
    password = CharField(max_length=255)
    role = CharField()