from tkinter import *
from tkinter import ttk

from Controllers.UserController import *
from Controllers.TaskController import *
from Controllers.CategoryController import *


class UserView(Tk):
    def __init__(self):
        super().__init__()

        # Атрибуты окна
        self.title("Модуль отчётности (Специалист и Администратор)")
        self.geometry("1280x850")