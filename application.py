from frame import SimpleFrame
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
