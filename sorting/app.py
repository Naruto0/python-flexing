from tkinter import (
    Tk, Canvas, Button, StringVar,
    Frame, OptionMenu, Entry, ALL
    )
from random import shuffle

from algorythms import *

RANDOM_RANGE = (48, 256, 8)
# RANDOM_RANGE = (60, 260, 20)

SORTING_METHODS = {
    'bubble': bubble,
    'selection': selection,
    'insertion': insertion
    }

SORTING_SPEED = {
    'super-fast' : 10,
    'fast': 25,
    'normal': 125,
    'slow': 255,
    'ultra-slow': 500
}

BAR_SPACING = 12
BAR_OFFSET = 4


def generate(rng):
    """Make random range"""
    li = [i for i in range(*rng)]
    shuffle(li)
    return li


class ListObject(list):
    def __init__(self, iterable):
        super().__init__(iterable)
        self.source = iterable
        self.master = None
        self.clear()

    def initialize(self, master):
        self.master = master
        self.create_from_list(self.source)

    def create_from_list(self, source):
        self.clear()
        for index, value in enumerate(source):
            self.append(
                Rectangle(self.master, value, index)
            )
        self.render_sorted()
    
    def render_sorted(self):
        for bar in self:
            bar.move(bar.index * BAR_SPACING + BAR_OFFSET)
        self.master.update()
    
    def refresh_indexes(self):
        for index, rect in enumerate(self):
            rect.set_index(index)


class Rectangle:
    """rectangle item"""
    def __init__(self, master, value, index):
        self.master = master
        self.value = value
        self.index = index
        self.obj = master.create_rectangle(
            0, 0, 8,
            self.value,
            fill="blue"
            )
        self.init_pos = self.master.coords(self.obj)
    
    def get_position(self):
        return self.master.coords(self.obj)

    def set_index(self, value):
        self.index = value

    def __str__(self):
        return "{0}{{'value':{1},'index':{2}}}".format(
            self.__class__.__name__, self.value, self.index)
    
    def move(self, moveX):
        a, c = self.init_pos[0] + moveX, self.init_pos[2] + moveX
        self.master.coords(self.obj, (a, 0, c, self.value))

    def get(self):
        return self.obj
    
    def __lt__(self, other):
        return self.value < other.value

    def __gt_(self, other):
        return self.value > other.value
    
    def position(self, *args):
        return self.master.coords(self.obj, *args)

    def color(self, color):
        self.master.itemconfig(self.obj, fill=color)
        self.master.update()


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
