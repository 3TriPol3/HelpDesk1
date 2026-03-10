from tkinter import *
from tkinter import ttk

from Controllers.UserController import *
from Controllers.TaskController import *
from Controllers.CategoryController import *


class UserView(Tk):
    def __init__(self):
        super().__init__()

        # Атрибуты окна
        self.title("Управление заявками (Пользователь)")
        self.geometry("1280x850")