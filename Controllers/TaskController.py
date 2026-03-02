from Models.Task import Task

class TaskController:
    '''
    Класс для работы с заявками
    Реализация CRUD
    '''

    @classmethod
    def add(cls, topic, description, path, priority='Низкий', status='Новая'):  # Create
        '''
        Добавление заявки
        :param topic: тема
        :param description: описание
        :param path: путь
        :param priority: приоритет
        :param status: статус
        :return:
        '''
        try:
            Task.create(
                topic=topic,
                description=description,
                path=path,
                priority=priority,
                status=status
            )
            return f'Заявка: <{topic}>, со статусом: <{status}>, добавлена'
        except:
            print("Ошибка добавления заявки!!!")

    @classmethod
    def get(cls): # Read
        '''
        Вывод списка заявок из таблицы Task
        :return:
            список заявок (объект)
        '''
        return Task.select()

    @classmethod
    def update(cls,id,**kwargs): # Update
        '''
        :param id: по id заявки будет происходить изменение занчений записи в таблицы
        :param kwargs: вводится название поля и его новое значение
                за один вызов метода можно изменить несколько полей одной записи
        :return:
            возвращаем сообщение об изменениях заявки
            если ошибка - возвращаем текст ошибки
        '''
        try:
            for key, value in kwargs.items():# key - название столбца/поля, value - новое значение,  kwargs.items() - аргументы в виде списка словарей
                Task.update({key:value}).where(Task.id == id).execute()
            return f'У заявки изменен {kwargs} на {kwargs[key]} '
        except :
            return 'Ошибка измениния заявки'

    @classmethod
    def delete(cls, id):    # Delete
        '''
        Удаление заявки по id
        :param id: id заявки
        :return:
        '''
        Task.delete_by_id(id)


    # @classmethod
    # def auth(cls,login,password):
    #     '''
    #     :param login:
    #     :param password:
    #     :return:
    #     '''
    #     # task = Task.select().where(Task.login == login)[0]
    #     task = Task.get_or_none(Task.login==login)
    #     if task:
    #         hash_password = task.password
    #         if checkpw(password.encode('utf-8'),hash_password.encode('utf-8')):
    #             return "Есть такой пользователь"
    #
    #     return 'Неверный логин или пароль'
    #
    # @classmethod
    # def test_hesh(cls, password):
    #     '''
    #     Хештруем пароль password
    #     :param password: пароль
    #     :return:
    #     '''
    #     print(password)
    #     password = bytes(password,'utf-8')
    #     hashed = hashpw(password,gensalt())
    #     print(hashed)
    #     if checkpw(password,hashed):
    #         print('Работет')


if __name__ == "__main__":
    # print(TaskController.add(     # Create
    #     topic='Не работает принтер',
    #     description='принтер перестал работать',
    #     path='С/User/ProgramFiles'
    # ))

    for row in TaskController.get():    # Read
        print(row.id, row.topic, row.description, row.path, row.priority, row.status)

    # print(TaskController.update(3,priority = "Высокий"))      # Update
    # print(TaskController.update(2, status="В работе"))    # Update

    # print(TaskController.delete(2))   # Delete



