from tkinter import Label


class SimpleLabel:
    def __init__(self):
        print('this is label.')

    def add(self, root: object, *, name: str=None, row: int=None, column: int=None):
        label = Label(master=root, text=name)
        label.grid(row=row, column=column)
        print('add method called.\nbutton name: '+name)

