#!/usr/bin/python3
'''This is a script generated documentation'''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Pending documentation'''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        elif size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.width))

    '''def update(self, *args, **kwargs):
        if args:
            if len(args) >= 1:
                self.id = args[0] if args[0] is not None else self.id
            if len(args) >= 2:
                self.width = args[1] if args[1] is not None else self.width
                self.height = self.width
            if len(args) >= 3:
                self.x = args[2] if args[2] is not None else self.x
            if len(args) >= 4:
                self.y = args[3] if args[3] is not None else self.y

        if not args or args is None:
            if "id" in kwargs:
                self.id = kwargs["id"] if kwargs["id"] is not None else self.id
            if "size" in kwargs:
                self.width = (kwargs["size"] if kwargs["size"]
                            is not None else self.width)
                self.height = self.width
            if "x" in kwargs:
                self.x = kwargs["x"] if kwargs["x"] is not None else self.x
            if "y" in kwargs:
                self.y = kwargs["y"] if kwargs["y"] is not None else self.y

    def to_dictionary(self):
        return self.__dict__'''
