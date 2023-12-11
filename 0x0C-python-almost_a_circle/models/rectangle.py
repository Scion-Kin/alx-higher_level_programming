#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    '''def area(self):
        return self.__height * self.__width

    def display(self):
        print(""*self.__y)
        for i in range(self.__height):
            print(" "*self.__x, end="")
            print("#"*self.__width, end="")
            print()

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        if args:
            if len(args) >= 1:
                self.id = args[0] if args[0] is not None else self.id
            if len(args) >= 2:
                self.__width = args[1] if args[1] is not None else self.__width
            if len(args) >= 3:
                self.__height = (args[2] if args[2] is not None
                                else self.__height)
            if len(args) >= 4:
                self.__x = args[3] if args[3] is not None else self.__x
            if len(args) >= 5:
                self.__y = args[4] if args[4] is not None else self.__y

        if not args or args is None:
            if "id" in kwargs:
                self.id = kwargs["id"] if kwargs["id"] is not None else self.id
            if "width" in kwargs:
                self.__width = (kwargs["width"] if kwargs["width"] is not None
                                else self.__width)
            if "height" in kwargs:
                self.__height = (kwargs["height"] if kwargs["height"]
                                is not None else self.__height)
            if "x" in kwargs:
                self.__x = kwargs["x"] if kwargs["x"] is not None else self.__x
            if "y" in kwargs:
                self.__y = kwargs["x"] if kwargs["x"] is not None else self.__y

    def to_dictionary(self):
        return self.__dict__'''
