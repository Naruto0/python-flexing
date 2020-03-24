# Triangle problem

_.. with `Typing` Yaaay!_

## Task

Given three _points_ `Point(x,y)` in the two-dimensional space,
count the perimter of 
triangle `Triangle[Point(x,y),Point(x1,y1),Point(x2,x3)]`.

We can simply write a function to do this for us following the rule
that not for every problem we need to create `class`.

However, as we can see this task originates in some typed language
_(most probablyJava)_ we will definitely make them.

As we are doing `class` for each object, we also can incorporate `typing`,
to better undesrtand what `arguments` are passed to which `class`,
so our _linting plugins_ in our `IDE` or `mypy` should recognize any error before
even importing the module.

You can see there are some complications with `typing`, yet those are good and
mostly helpful complications. At least for understanding _inheritance_.

### Brainstorm

We need following classes:
_(there definitely be other ones, but for now...)_

- `Point()` to manage point in two dimensional space
- `Triangle()` to hold the points of a triangle and required method `get_perimeter()`

For each class, we also override ``__str__(self)`` function to see

#### ``Point(x: float, y: float):``

Eventought we can use `int` (just for simplification) `float` makes
better sense anyway.

We will need to count length of a side. We can definitely make
this a _method_ of a `Point()`. For example `get_distance()`.
But let's not rush too fast.

_With future project we may reuse point with any other `class`, so it eventually
be it's own module..._

#### ``Triangle(a: Point, b: Point, c: Point):``

Using `Point()`s own method, we can make lenght of triangle sides.

### To the code

Choose your `IDE`, setup `.virtualenv` and let's start some snippets...

```python
class Point:
    def __init__(self, *args):
        super().__init__()
        self.x, self.y = args
```

Altought we can start more pythonic way, we rather _duck-type_ the arguments there
and make it clear that it is a pair of values.

Let's also override ``__str__()`` function to have more beauty in console..

```python
from typing import Any

class Point:
    def __init__(self, x: float, y: float):
        self.x, self.y = x, y

    def __str__(self) -> Any:
        return f'{self.__class__.__name__}({self.x},{self.y})'
```

Let's run interpreter and try it out..

```python
>>> from triangle import Point
>>> p = Point(14,5)
... # Now let's make another one
>>> p2 = Point(12,4)
... # We can access each attribute of a point
... # we do not have any use for that
>>> p.x
14
>>> p2.y
4
... # Regarding the `__str__` tough..
>>> print(p)
Point(14,5)
```

Now we have two points. How can we measure the distance between them?
Let's use the basic math from school and use Pythagorean Theorem.

```python
from math import sqrt
# ...


class Point:
    # ...
    def get_distance(self, other: Point):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    # ...

```

Now, let's try it out...

```python
>>> from triangle import Point
## ---> 13     def get_distance(self, other: Point):
## NameError: name 'Point' is not defined

```

Well, that is not we use to encounter with `java`. Seems we can't refer to
a class inside itself, even my `flake8` does not agree.
We do not want create new type either.

As there is no _interface_ in `python`,
we simply make one. Not full flagged interface, yet some useful simple prototype.
We need Point to have an _ancestor_,
so that the `other` function can be compatibile with `Point()` to a degree.

Let's try this out:

We move ``__init__()`` and ``__str__()`` methods to ``PointProto()``:

```python
# ...
class PointProto:
    """Point class prototype"""
    def __init__(self, x: float, y: float):
        self.x, self.y = x, y

    def __str__(self) -> Any:
        return f'{self.__class__.__name__}({self.x}, {self.y})'
```

And recreate ``Point()`` to inherit from newly created _class_:

```python
# ...
class Point(PointProto):
    """Point class"""
    def __init__(self, x: int, y: int):
        PointProto.__init__(self, x, y) # init ancestor class

    def get_distance(self, other: PointProto) -> float:
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    # as we inherit `__str__()` method, we need it no longer here
```

Let's try that out now.

```python
>>> from trinagle import Point
>>> p1 = Point(14,5)
>>> p2 = Point(7,8)
>>> d = p1.get_distance(p2)
>>> d
7.615773105863909
```

Before we wrap it up with display of the whole code, let's have
the triangle class first. Nothing complicated, just incorporate
what you've seen above.

```python
# ...
class Triangle(object):
    """Triangle object"""
    def __init__(self, a: Point, b: Point, c: Point):
        super().__init__()
        self.a, self.b, self.c = a, b, c

    def __str__(self) -> Any:
        return f'{self.__class__.__name__}[{self.a}, {self.b}, {self.c}]'

    def get_perimeter(self) -> float:
        # as you can see, we use a's method so
        # the ab side gets measured by passing b side as argument to it
        perimeter = self.a.get_distance(self.b) + \
            self.b.get_distance(self.c) + self.c.get_distance(self.a)

        return perimeter
        # we may return the value right away, yet this more convenient for
        # debugging purposes also
```

Now to the fun:

```python
>>> from triangle import Point, Triangle
>>> p1, p2, p3 = Point(8, 16), Point(32, 48), Point(16, 8)
>>> t = Triangle(p1, p2, p3)
>>> print(t)
Triangle[Point(8, 16), Point(32, 48), Point(16, 8)]
>>> t.get_perimeter()
94.3950269560608
```

## Conclusion

Our `Trinagle()` is really not very useful class. Making class just to resolve _one_
problem is not considered _good practice_. However we can make more similar objects,
wrap it under `Shape()` and incorporate `Point()` to each and we can measure
distance between points swiftly.

- Do not overuse `class`, rather use `function()`
- Try `typing` along with `mypy` in python and help yourself to understand
_typed language_ of your friend while teaching him/her `python`.
- Make a game.
