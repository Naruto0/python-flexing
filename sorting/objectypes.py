from sorting.settings import BAR_OFFSET, BAR_SPACING

__all__ = ['ListObject', 'Rectangle']


class ListObject(list):
    def __init__(self, iterable, strict=True):
        super().__init__(iterable)
        self.source = iterable
        self.master = None
        self.strict = strict
        self.clear()
        if not strict:
            self.create_from_list(self.source)

    def initialize(self, master):
        self.master = master
        self.create_from_list(self.source)

    def create_from_list(self, source):
        self.clear()
        if all([isinstance(o, Rectangle) for o in source]):
            for item in source:
                self.append(item)
                self.master = item.master
        else:
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
        """Refresh indexes in absolute or relative"""
        if self.strict:
            for index, rect in enumerate(self):
                rect.set_index(index)
        else:
            indexes = sorted([i.index for i in self])
            for index, rect in zip(indexes, self):
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
