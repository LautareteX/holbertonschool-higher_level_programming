#!/usr/bin/python3
"""
Reviewing all subjects
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self._Rectangle__width

    @property
    def x(self):
        return self._Rectangle__x

    @property
    def y(self):
        return self._Rectangle__y

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value <= 0:
            raise ValueError("size must be > 0")
        self._Rectangle__width = value
        self._Rectangle__height = value

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self._Rectangle__y = value

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self._Rectangle__x = value

    def update(self, *args, **kwargs):
        """allocation of values in order or by dictionary"""
        if args:
            for iterator, count in enumerate(args, start=1):
                if iterator == 1:
                    self.id = count
                if iterator == 2:
                    self.size = count
                if iterator == 3:
                    self.x = count
                if iterator == 4:
                    self.y = count
        else:
            for iterator, count in kwargs.items():
                if iterator == "id":
                    self.id = count
                if iterator == "size":
                    self.size = count
                if iterator == "x":
                    self.x = count
                if iterator == "y":
                    self.y = count

    def to_dictionary(self):
        """ Rectange dictionary representation """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
