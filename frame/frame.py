from frame.widgets import SimpleLabel, SimpleButton
from tkinter import Frame

class SimpleFrame:
    def __init__(self, root):
        self.root = root
        self.widgets_list = list()
        self.frame = Frame(self.root)
    
    def label(self, name, row: int=None, column: int=None):
        label = SimpleLabel()
        label.add(self.frame, name=name, row=row, column=column)
        self.widgets_list.append(label)

    def button(self, name, row: int=None, column: int=None):
        button = SimpleButton()
        button.add(self.frame, name=name, row=row, column=column)
        self.widgets_list.append(button)

    def set_frame(self, row: int=None, column: int=None):
        self.frame.grid(row=row, column=column)

    def show(self):
        return self.widgets_list

