import peewee
from peewee import *

# Первый способ
# mysql_db = MySQLDatabase('BessM82_HelpDesk',
#                          user='BessM82_HelpDesk',
#                          password='111111',
#                          host='10.11.13.118')

# Второй способ
def connect():
    try: # Удачная попытка
        mysql_db = MySQLDatabase('BessM82_HelpDesk',
                                 user='BessM82_HelpDesk',
                                 password='111111',
                                 host='10.11.13.118')
        return mysql_db
    except: # Неудачная попытка
        print(f'Ошибка')
        return None


if __name__ == "__main__":
    print(connect().connect())