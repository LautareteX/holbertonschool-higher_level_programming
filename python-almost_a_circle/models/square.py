#!/usr/bin/python3
"""
Reviewing all subjects
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor clase"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - " \
            f"{self.width}"
