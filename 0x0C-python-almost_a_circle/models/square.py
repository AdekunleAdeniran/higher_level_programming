#!/usr/bin/python3

'''Square class module'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Instantiate Square class attributes'''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''print attribute with __str__'''
        a, b, c, d = self.id, self.x, self.y, self.size
        return ("[Square] ({}) {}/{} - {}".format(a, b, c, d))

    def update(self, *args, **kwargs):
        '''Set up args for rectangle'''
        if len(args) != 0:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.size = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
        else:
            for key, values in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, values)

    @property
    def size(self):
        """set the property of width"""
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.width = value

    def to_dictionary(self):
        '''Method to return dictionary representation of square'''
        dic = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return dic
