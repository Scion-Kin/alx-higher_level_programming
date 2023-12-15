#!/usr/bin/python3
"""This module creates a class definition."""
from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Defines instance attributes'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''This is the getter of the private width attribute'''
        return self.__width

    @width.setter
    def width(self, value):
        '''This is the setter of the private width attribute'''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''This is the getter of the private height attribute'''
        return self.__height

    @height.setter
    def height(self, value):
        '''This is the setter of the private height attribute'''
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''This is the getter of the private x attribute'''
        return self.__x

    @x.setter
    def x(self, value):
        '''This is the setter of the private x attribute'''
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''This is the getter of the private y attribute'''
        return self.__y

    @y.setter
    def y(self, value):
        '''This is the setter of the private y attribute'''
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''Returns the area of the rectangle'''
        return self.width * self.height

    def display(self):
        '''Prints the Rectangle using the `#` character.'''
        if self.width == 0 or self.height == 0:
            print()
            return

        print(""*self.y)
        for h in range(self.height):
            print(" "*self.x, end="")
            print("#"*self.width, end="")
            print()

    def update(self, *args, **kwargs):
        '''Updates the instance attributes with provided arguments'''
        if args:
            if len(args) >= 1:
                self.id = args[0] if args[0] is not None else self.id
            if len(args) >= 2:
                self.width = args[1] if args[1] is not None else self.width
            if len(args) >= 3:
                self.height = args[2] if args[2] is not None else self.width
            if len(args) >= 4:
                self.x = args[3] if args[3] is not None else self.x
            if len(args) >= 5:
                self.y = args[4] if args[4] is not None else self.y

        elif kwargs and len(kwargs) != 0:
            if "id" in kwargs:
                self.id = kwargs["id"] if kwargs["id"] is not None else self.id
            if "width" in kwargs:
                self.width = (kwargs["width"] if kwargs["width"]
                              is not None else self.width)
            if "height" in kwargs:
                self.height = (kwargs["height"] if kwargs["height"]
                               is not None else self.height)
            if "x" in kwargs:
                self.x = kwargs["x"] if kwargs["x"] is not None else self.x
            if "y" in kwargs:
                self.y = kwargs["y"] if kwargs["y"] is not None else self.y

    def to_dictionary(self):
        '''Returns the dictionary representation of the class instance'''
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
