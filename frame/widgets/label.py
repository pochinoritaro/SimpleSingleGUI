
class SimpleLabel:
    def __init__(self):
        print('this is label.')

    def add(self, root: object, *, name: str=None, row: int=None, column: int=None):
        button = Button(master=root, text=name)
        button.grid(row=row, column=column)
        print('add method called.\nbutton name: '+name)

