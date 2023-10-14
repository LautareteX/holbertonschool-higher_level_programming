#!/usr/bin/python3
""" Square class with methods """
from models.rectangle import Rectangle


class Square(Rectangle):
    """My Simple Square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Get a string representation of the rectangle."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Get the size of the square"""
        return self.width

    @size.setter
    def size():
        """Get the size of the square"""
        pass
