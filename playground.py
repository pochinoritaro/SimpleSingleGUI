from tkinter import Button
from tkinter import Label
from tkinter import Frame
from tkinter import Tk


class SimpleGui:
    def __init__(self):
        self.frame_list = list()
        self.root = Tk()

    def create_frame(self):
        frame = SimpleFrame(self.root)
        self.frame_list.append(frame)
        return frame

    def run(self):
        self.root.mainloop()

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

class SimpleLabel:
    def __init__(self):
        print('this is label.')

    def add(self, root: object, *, name: str=None, row: int=None, column: int=None):
        label = Label(master=root, text=name)
        label.grid(row=row, column=column)
        print('add method called.\nbutton name: '+name)


class SimpleButton:
    def __init__(self):
        print('this is button.')

    def add(self, root: object, *, name: str=None, row: int=None, column: int=None):
        button = Button(master=root, text=name)
        button.grid(row=row, column=column)
        print('add method called.\nbutton name: '+name)


if __name__ == "__main__":
    gui = SimpleGui()
    form = gui.create_frame()
    form.label(name='name', row=0, column=0)
    form.button(name='name', row=0, column=1)
    form.button(name='name2', row=1, column=0)
    form.set_frame(0, 0)
    fm = form.show()
    print(fm)
    gui.run()
