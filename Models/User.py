from Models.Base import *

class User(BaseModel):
    id = PrimaryKeyField()
    login = CharField(unique=True, max_length=10)
    password = CharField(max_length=255)
    role = CharField(choices=[
        'Пользователь',
        'Администратор',
        'Специалист техподдержки'
    ])
    is_active = BooleanField(default=True) # Альтернатива удаления
    fullname = CharField(null=True, max_length=150)
