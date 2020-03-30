from tkinter import (
    Tk, Canvas, Button, StringVar,
    Frame, OptionMenu, ALL
    )
from random import shuffle

from sorting.objectypes import ListObject
from sorting.settings import SORTING_SPEED, RANDOM_RANGE

from sorting.algos import SORTING_METHODS


def generate(rng):
    """Make random range"""
    li = [i for i in range(*rng)]
    shuffle(li)
    return li


class CanvasFrame(Frame):
    """Drawing area"""
    def __init__(self, master=None, **kw):
        super().__init__(master=master)
        self.canvas = Canvas(self, relief="sunken")
        self.bars = ListObject(
            generate(RANDOM_RANGE)
            )
        self.bars.initialize(self.canvas)
        self.canvas.pack(side="bottom")

    def clean(self):
        self.canvas.delete(ALL)


class ControlBar(Frame):
    """Control bar holds buttons and method option menu"""
    def __init__(self, master=None, *kw):
        super().__init__(master=master)
        # children items
        self.btn_gen = Button(self, text="Generate", command=master.generate)
        self.btn_sort = Button(self, text="Sort", command=master.sort)
        self.method_menu = OptionMenu(
            self, master.method,
            *master.method_choices)
        self.speed_menu = OptionMenu(
            self, master.speed,
            *master.speed_ch)
        # packing
        self.btn_gen.pack(side="left")
        self.btn_sort.pack(side="left")
        self.method_menu.pack(side="right")
        self.speed_menu.pack(side="right")

    def set_active(self, state):
        self.btn_gen['state'] = 'active' if state else 'disabled'


class Application(Frame):
    """Main window Frame"""
    def __init__(self, master=None, **kw):
        super().__init__(master=master)
        # variables
        self.method = StringVar()
        self.method.set("insertion")
        self.method_choices = {k for k in SORTING_METHODS.keys()}
        self.speed = StringVar()
        self.speed.set("slow")
        self.speed_ch = {k for k in SORTING_SPEED.keys()}
        # graphics
        self.canvas_frame = CanvasFrame(self)
        self.control_frame = ControlBar(self)
        self.canvas_frame.pack(side="top")
        self.control_frame.pack(side="bottom")
    
    def initial(self):
        pass
    
    def generate(self, *args):
        self.canvas_frame.clean()
        self.canvas_frame.bars.create_from_list(generate(RANDOM_RANGE))

    def sort(self, *args):
        self.control_frame.set_active(False)
        method = SORTING_METHODS[self.method.get()]
        speed = SORTING_SPEED[self.speed.get()]
        method(self, self.canvas_frame.bars, speed)
        self.control_frame.set_active(True)


def main():
    main_window = Tk()
    app_window = Application(main_window)
    app_window.pack()
    main_window.mainloop()


if __name__ == '__main__':
    main()
