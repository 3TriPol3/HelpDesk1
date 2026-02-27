from Models.Base import *

class Category(BaseModel):
    id = PrimaryKeyField()
    name = CharField(unique=True, max_length=150)
    category_id = ForeignKeyField()

