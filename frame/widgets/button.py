from tkinter import Button

class SimpleButton:
    def __init__(self):
        print('this is button.')

    def add(self, root: object, *, name: str=None, row: int=None, column: int=None):
        button = Button(master=root, text=name)
        button.grid(row=row, column=column)
        print('add method called.\nbutton name: '+name)
