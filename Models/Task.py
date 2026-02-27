from Models import User
from Models.Base import *

class Task(BaseModel):
    id = PrimaryKeyField()
    topic = CharField(max_length=100)
    description =  TextField()
    path = CharField(max_length=255) # Путь к файлу в папке на сервере
    priority = CharField(choices=[
        'Низкий',
        'Средний',
        'Высокий'
    ])
    status = CharField(choices=[
        'Новая',
        'В работе',
        'Выполнена'
    ])
    user_id = ForeignKeyField(model=User)
    speciality_id = ForeignKeyField(model=User)
    category_id = ForeignKeyField(model=Category)
