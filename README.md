# Информационная система «Техническая поддержка» #
## Наименование проекта ##
*Полное наименование: **Информационная система «Техническая поддержка»(HelpDesk)**.*
_Краткое наименование: __ИС «TechSupport»__._

## **План** ##
1. [x] ~~Создать диаграмму~~
2. [x] ~~Создать базу данных~~
3. [x] ~~Разработать структуру проекта~~
4. [ ] Написать код в соответствии со структурой

### Диаграммы ###
Созданы диаграммы Вариантов использования и Классов.

### База данных ###
Создана База данных из **трёх сущностей:**
+ _**User**_
    1. id(int:11)
    2. login(varchar:12)
    3. password(varchar:255)
    4. role:
       Можно выбрать из трёх вариантов:
       - 'Пользователь',
       - 'Администратор',
       - 'Специалист'
    5. is_active
    6. fullname(varchar:150)
    
+ _**Task**_
    1. id(int:11)
    2. topic(varchar:100) 
    3. description
    4. path(varchar:255) 
    5. priority:
       Можно выбрать из трёх вариантов:
       - 'Низкий',
       - 'Средний',
       - 'Высокий'
    6. status:
       Можно выбрать из трёх вариантов:
       - 'Новая',
       - 'В работе',
       - 'Выполнена'
    7. user_id
    8. speciality_id
    9. category_id

+ _**Category**_
    1. id(int:11)  
    2. name(varchar:150)


### Структура проекта ###
```commandline
HelpDesk1/
|--Connection/
|   |--connect.py                       # Подключение к БД
|--Controllers/
|   |--UserController.py                # Контроллер для работы с пользователем    
|   |--CategoryController.py            # Контроллер для работы с категориями заявок 
|   |--TaskController.py                # Контроллер для работы с заявками 
|--Models/
|   |--Base.py                          # Базовая Модель
|   |--Category.py                      # Модель для описания таблицы Категорий
|   |--create_table.py                  # Создание таблицы
|   |--Task.py                          # Модель для описания таблицы Заявок
|   |--User.py                          # Модель для описания таблицы Пользователей
|--Views/
|   |--HelpDesk1_view.py                # Главное Окно
|--main.py                              # Главный файл запуска
|--README.md                            # Файл описания работы 
|--requirements.txt                     # Файл с названиями библиотек
```


### Технологии ###
- **Python** - основной язык программирования
- **Peewee** - ORM для работы с Базой данных
- **MySQL** - Система управления БД (СУБД)
- **PyMysql** - библиотека для подключения к СУДБ
- **Tkinter** - библиотека для создания графических интерфейсов (GUI)
- **bcrypt** - библиоткека для хеширования паролей


### Модели ###
#### User (Пользователи) ####
- `id` - Первичный ключ
- `login` - Логин уникальный, максимум 12 символов
- `password` - Хешированный пароль, максимум 255 символов
- `role` - Роль пользователя: 'Пользователь', 'Администратор', 'Специалист'
- `is_active` - При создании True, Альтернатива удаления
- `fullname` - Полное имя пользователя, максимум 150 символов
- #### Task (Заявки) ####
- `id` - Первичный ключ
- `topic` - Тема заявки, максимум 100 символов
- `description` - Описание заявки
- `path` - Путь, максимум 255 символов
- `priority` - Приоритет заявки
- `status` - Статус заявки
- `user_id` - Ссылка на таблицу пользователей
- `speciality_id` - Ссылка на таблицу Специалистов
- `category_id` - Ссылка на таблицу Категорий
#### Category (Категории) ####
- `id` - Первичный ключ
- `name` - Название категории, максимум 150 символов


## Установка ##
1. Все библиотеки указаны в файле `requirements.txt`
2. Подключение к БД в `HelpDesk1/Connection/connect.py`
3. Создать таблицы в БД с помощью
    ```bash
    python HelpDesk1/Models/create_table.py 
    ```


## Функционал кода ##
### Работа с пользователями ###
Отвечает **UserController**
```python
from Controllers.UserController import UserController
# Регистрация пользователя Администратор
UserController.registration(    # Create
        login='admin2',
        password='admin2'
    )

# Вывод списка пользователей
for row in UserController.get():  # Read
    print(row.id, row.login, row.password, row.role, row.is_active, row.fullname)
    
# Обновить данные пользователя
UserController.update(2,login = "admin2")   # Update

# Удаление пользователей
UserController.delete(2)    # Delete

# Авторизация
print(UserController.auth('user','user'))

# Тест хэша
UserController.test_hesh('1234')


```

### Работа с заявками ###
Отвечает **TaskController**
```python
from Controllers.TaskController import TaskController
# Создание новой заявки
print(TaskController.add(     # Create
    topic='Не работает принтер',
    description='принтер перестал работать',
    path='С/User/ProgramFiles'
))

# Вывод списка пользователей
for row in TaskController.get():    # Read
    print(row.id, row.topic, row.description, row.path, row.priority, row.status)
    
# Обновить данные заявки    
TaskController.update(3,priority = "Высокий")   # Update

# Удаление заявок
TaskController.delete(1) # Delete

```

### Работа с категориями ###
Отвечает **CategoryController**
```python
from Controllers.CategoryController import CategoryController
# Создание новой категории
print(CategoryController.add(     # Create
    name='ПК'
))

# Вывод списка категорий
for row in CategoryController.get():    # Read
    print(row.id, row.name)
    
# Обновить данные категории    
CategoryController.update(2, name="Техника")    # Update

# Удаление категорий
CategoryController.delete(1)    # Delete

```


## Лицензия ##
Проект находится **в разработке** 
