from tkinter import *
from tkinter import ttk

from Controllers.UserController import *


class UserView(Tk):
    def __init__(self):
        super().__init__()

        # Атрибуты окна
        self.title("Авторизация")
        self.geometry("1280x850")
