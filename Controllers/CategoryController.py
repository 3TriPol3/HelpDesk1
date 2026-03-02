from Models.Category import Category

class CategoryController:
    '''
    Класс для работы с категориями
    Реализация CRUD
    '''

    @classmethod
    def add(cls, name): # add
        '''
        Добавление категории
        :param name: Название категории
        :return:
        '''
        try:
            Category.create(
                name=name
            )
            return f'Категория: <{name}>, добавлена'
        except:
            print("Ошибка добавления категории!!!")

    @classmethod
    def get(cls):  # read
        '''
        Вывод списка категорий из таблицы Category
        :return:
            список категорий (объект)
        '''
        return Category.select()

    @classmethod
    def update(cls,id,**kwargs): # update
        '''
        :param id: по id категории будет происходить изменение значений записи в таблицы
        :param kwargs: вводится название поля и его новое значение
                за один вызов метода можно изменить несколько полей одной записи
        :return:
            возвращаем сообщение об изменениях категории
            если ошибка - возвращаем текст ошибки
        '''
        try:
            for key, value in kwargs.items():# key - название столбца/поля, value - новое значение,  kwargs.items() - аргументы в виде списка словарей
                Category.update({key:value}).where(Category.id == id).execute()
            return f'У категории изменено {kwargs} на {kwargs[key]} '
        except :
            return 'Ошибка измениния категории!!!'

    @classmethod
    def delete(cls, id):
        '''
        Удаление категории по id
        :param id: id категории
        :return:
        '''
        Category.delete_by_id(id)


if __name__ == "__main__":
    # print(CategoryController.add(     # Create
    #     name='ПК'
    # ))

    for row in CategoryController.get():    # Read
        print(row.id, row.name)

    print(CategoryController.update(2, name="Техника"))     # Update

    # print(CategoryController.delete(2))   # Delete

