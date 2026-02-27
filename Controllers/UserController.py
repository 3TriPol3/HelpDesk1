from Models.User import User


class UserController:
    '''
    Класс для работы с пользователем
    Реализация CRUD
    '''
    @classmethod
    def get(cls):
        '''
        Вывод списка пользователей из таблицы User
        :return:
            список пользователей (объект)
        '''
        return User.select()

    @classmethod
    def registration(cls, login, password, role = 'Пользователь'): # add
        '''

        :param login: логин пользователя, не более 10 символов, должен быть уникален
        :param password: пароль в будущем должен быть в виде HASH пароль
        :param role: Роль в системе, если не указана, то: "Пользователь"
        :return:
            если ошибка - возвращаем текст ошибки
            иначе - возвращаем сообщение о созданном пользователе
        '''
        try:
            User.create(
                login = login,
                password = password,
                role = role
            )
            return f'Пользователь {login} с ролью {role} добавлен'
        except:
            return 'Ошибка добавления пользователя'

    @classmethod
    def update(cls, id, **kwargs):
        '''

        :param id: по id пользователя будет происходить изменение значений записи в таблице
        :param kwargs: Вводится название поля и его новое значение (например: login = "новый_логин")
                за один вызов метода можно изменить несколько полей одной записи
        :return:
            возвращаем сообщение об изменениях пользователя
            если ошибка - возвращаем текст ошибки
        '''
        try:
            for key, value in kwargs.items(): # key - название столбца/поля, value - новое значение, kwargs.items() - аргументы в виде списка словарей
                User.update({key:value}).where(User.id == id).execute()
            return f'У Пользователя изменён {kwargs} на {id} '
        except:
            return 'Ошибка изменения пользователя'
    @classmethod
    def update_status(cls, id):
        '''
        меняет у потльзователя статус с True на False и c False на True
        :param id: id пользователя
        :return:
            новый статус пользователя
        '''
        status = User.get_by_id(id).is_active # Получаем по id пользователя его значения поля is_active (True/False)
        User.update({User.is_active:not status}).where(User.id==id).execute()
        return f'Статус пользователя стал {status}'

    @classmethod
    def auth(cls, login, password):
        '''

        :param login:
        :param password:
        :return:
        '''
        user = User.select().where(User.login == login)[0]
        if user:
            if user.password == password:
                return "Есть такой пользователь"
        return 'Неверный логин или пароль'


if __name__ == "__main__":
    # print(UserController.registration(
    #     login='admin1',
    #     password='admin',
    #     role='Администратор'
    # ))
    # print(UserController.update(1, login="admin"))
    # print(UserController.update_status(2))
    print(UserController.auth('admin', 'admin'))
    # for row in UserController.get():
    #     print(row.id, row.login, row.password, row.role, row.is_active, row.fullname)

