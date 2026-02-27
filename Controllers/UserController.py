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





if __name__ == "__main__":
    print(UserController.registration(
        login='admin1',
        password='admin',
        role='Администратор'
    ))
    for row in UserController.get():
        print(row.id, row.login, row.password, row.role, row.is_active, row.fullname)