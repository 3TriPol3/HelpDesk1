from Connection.connect import *

class BaseModel(Model):
    class Meta: # Передаёт следующие метаданные
        database = connect()