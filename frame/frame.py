from frame.widgets import SimpleLabel, SimpleButton
from tkinter import Frame

class SimpleFrame:
    def __init__(self, root):
        self.root = root
        self.widgets_list = list()
        self.frame = Frame(self.root)
    
    def add_label(self):
        self.label = Label()
        self.widgets_list.append(self.label)
    
    def button(self, name, row: int=None, column: int=None):
        self.button = SimpleButton()
        self.button.add(self.root, name=name, row=row, column=column)
        self.widgets_list.append(self.button)

    def show(self):
        return self.widgets_list

