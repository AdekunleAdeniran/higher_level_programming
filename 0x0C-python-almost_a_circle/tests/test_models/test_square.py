#!/usr/bin/python3

""" Square Class TestCases """

from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import unittest
import sys          # for stdout access
import io           # for stdout printing tests


class SquareModelTestCase(unittest.TestCase):
    """ TestCases for Square Model
        Square(width, height, x, y, id) """

    def test_that_Square_inherits_from_Rectangle(self):
        """ Tests that Square inherits from Rectangle """
        x = Square(10)
        self.assertEqual(issubclass(Square, Rectangle), True)

    def test_Square_inherits_id_from_Base(self):
        """ Tests that id is inherited from base, it should never be None """
        x = Square(10, 10)
        self.assertEqual(x.id is None, False)
        x = Square(10, 10, id=None)
        self.assertEqual(x.id is None, False)

    def test_if_width_is_int(self):
        """ Checks if width is an int """
        x = Square(10, 10)
        self.assertEqual(type(x.width), int)

    def test_width_can_be_very_big(self):
        """ Checks that width can be max int """
        x = Square(sys.maxsize, 5)
        self.assertEqual(x.width, sys.maxsize)

    def test_raise_TypeError_if_size_is_not_int(self):
        """ Checks for TypeError exception if width is not an int """
        with self.assertRaises(TypeError):
            x = Square('9')

        exc_msg = 'width must be an integer'
        with self.assertRaises(TypeError) as msg:
            x = Square({})
        self.assertEqual(str(msg.exception), exc_msg)

        with self.assertRaises(TypeError) as msg:
            x = Square([4])
        self.assertEqual(str(msg.exception), exc_msg)

        with self.assertRaises(TypeError) as msg:
            x = Square((1,))
        self.assertEqual(str(msg.exception), exc_msg)

        with self.assertRaises(TypeError) as msg:
            x = Square({1: 'a', 2: 'b'})
        self.assertEqual(str(msg.exception), exc_msg)

    def test_if_size_is_int(self):
        """ Checks if height is an int """
        x = Square(10)
        self.assertEqual(type(x.size), int)

    def test_size_can_be_very_big(self):
        """ Checks that height can be max int """
        x = Square(sys.maxsize)
        self.assertEqual(x.size, sys.maxsize)

    def test_raise_ValueError_if_width_is_less_than_zero(self):
        """ Checks if width is greater than 0 """
        exc_msg = 'width must be > 0'
        with self.assertRaises(ValueError) as msg:
            x = Square(-9, 10, 4)
        self.assertEqual(str(msg.exception), exc_msg)

        with self.assertRaises(ValueError) as msg:
            x = Square(-23, 10, 4)
        self.assertEqual(str(msg.exception), exc_msg)

    def test_raise_ValueError_if_size_is_less_than_zero(self):
        """ Checks if height is greater than 0 """
        exc_msg = 'width must be > 0'
        with self.assertRaises(ValueError) as msg:
            x = Square(-10, 5, 5)
        self.assertEqual(str(msg.exception), exc_msg)

    def test_raise_ValueError_if_x_is_negative(self):
        """ Checks that ValueError is raised if x < 0 """
        exc_msg = 'x must be >= 0'
        with self.assertRaises(ValueError) as msg:
            x = Square(10, -20, 1, 1)
        self.assertEqual(str(msg.exception), exc_msg)

    def test_raise_ValueError_if_y_is_negative(self):
        """ Checks that ValueError is raised if y < 0 """
        exc_msg = 'y must be >= 0'
        with self.assertRaises(ValueError) as msg:
            x = Square(10, 20, -1, 'id')
        self.assertEqual(str(msg.exception), exc_msg)

    def test_x_can_be_very_big(self):
        """ Checks that x can be max int """
        x = Square(10, sys.maxsize)
        self.assertEqual(x.x, sys.maxsize)

    def test_size_can_be_very_big(self):
        """ Checks that size can be max int """
        x = Square(sys.maxsize)
        self.assertEqual(x.size, sys.maxsize)

    def test_area_method_returns_correct_value(self):
        """ Checks that area() returns width * height """
        x = Square(2)
        self.assertEqual(x.area(), 4)
        x = Square(1, 1, 80, 54)
        self.assertEqual(x.area(), 1)

    def test_area_method_returns_really_big_number(self):
        """ Checks that area() works with maxsize int """
        x = Square(sys.maxsize)
        self.assertEqual(x.area(), sys.maxsize * sys.maxsize)

    def test_display_prints_a_square(self):
        """ Checks that the display() method prints a Square """
        x = Square(2)
        output = io.StringIO()  # sets output to an io stream
        sys.stdout = output     # connects the stream to stdout file object
        x.display()
        sys.stdout = sys.__stdout__     # makes file object the sysytems stdout
        self.assertEqual('##\n##\n', output.getvalue())

        x = Square(4)
        output = io.StringIO()
        sys.stdout = output
        x.display()
        sys.stdout = sys.__stdout__
        self.assertEqual('####\n####\n####\n####\n', output.getvalue())

    def test_display_prints_a_square_with_coordinates(self):
        """ Checks that the display() method prints a Square """
        x = Square(2, 1, 1)
        output = io.StringIO()
        sys.stdout = output
        x.display()
        sys.stdout = sys.__stdout__
        self.assertEqual('\n ##\n ##\n', output.getvalue())

        x = Square(2, 2, 3)
        output = io.StringIO()
        sys.stdout = output
        x.display()
        sys.stdout = sys.__stdout__
        self.assertEqual('\n\n\n  ##\n  ##\n', output.getvalue())

        x = Square(2, 4, 3)
        output = io.StringIO()
        sys.stdout = output
        x.display()
        sys.stdout = sys.__stdout__
        self.assertEqual('\n\n\n    ##\n    ##\n', output.getvalue())

        x = Square(2, 2, y=3)
        output = io.StringIO()
        sys.stdout = output
        x.display()
        sys.stdout = sys.__stdout__
        self.assertEqual('\n\n\n  ##\n  ##\n', output.getvalue())

    def test_str_method_returns_proper_representation(self):
        """ Checks that __str__ is overwritten with specs representation """
        x = Square(4, 6, 2, 12)
        target = '[Square] ({}) {}/{} - {}'.format(
                x.id, x.x, x.y, x.size)
        self.assertEqual(str(x), target)

        x = Square(10, 50)
        target = '[Square] ({}) {}/{} - {}'.format(
                x.id, x.x, x.y, x.size)
        self.assertEqual(str(x), target)

    def test_update_args_get_set_correctly(self):
        """ Checks that the update() method updates the correct attributes.
            The order should be: id, width, height, x, y """
        x = Square(10, 10, 10, 10)
        x.update(40, 20)
        self.assertEqual(x.id, 40)
        self.assertEqual(x.size, 20)

        x = Square(5, 5, 5, 5)
        x.update(666)
        self.assertEqual(x.id, 666)
        self.assertEqual(x.size, 5)

        x = Square(1, 1)
        x.update(6, 10)
        self.assertEqual(x.id, 6)
        self.assertEqual(x.size, 10)
        self.assertEqual(x.x, 1)

        x = Square(1, 1)
        x.update(6, 10, 4, 0)
        self.assertEqual(x.id, 6)
        self.assertEqual(x.size, 10)
        self.assertEqual(x.x, 4)
        self.assertEqual(x.y, 0)

    def test_update_with_no_args(self):
        """ Tests that update should do nothing if there are no arguments """
        x = Square(10, 10)
        x.update()
        self.assertEqual(x.size, 10)
        self.assertEqual(x.x, 10)
        self.assertEqual(x.y, 0)

    def test_update_with_one_arg(self):
        """ Tests that update should update id if there is one argument """
        x = Square(10)
        x.update(666)
        self.assertEqual(x.id, 666)
        self.assertEqual(x.size, 10)
        self.assertEqual(x.x, 0)
        self.assertEqual(x.y, 0)

    def test_update_with_two_args(self):
        """ Tests that update should update id and size
            if there are two arguments """
        x = Square(10)
        x.update(15, 5)
        self.assertEqual(x.size, 5)
        self.assertEqual(x.id, 15)
        self.assertEqual(x.x, 0)
        self.assertEqual(x.y, 0)

    def test_update_with_three_args(self):
        """ Tests that update should update id, size, and x
            if there are three arguments """
        x = Square(10)
        x.update(5, 6, 7)
        self.assertEqual(x.id, 5)
        self.assertEqual(x.size, 6)
        self.assertEqual(x.x, 7)
        self.assertEqual(x.y, 0)

    def test_update_with_four_args(self):
        """ Tests that update should update id, size, x, and y
            if there are four arguments """
        x = Square(10, 10)
        x.update(5, 5, 5, 5)
        self.assertEqual(x.id, 5)
        self.assertEqual(x.size, 5)
        self.assertEqual(x.x, 5)
        self.assertEqual(x.y, 5)

    def test_update_with_more_than_4_args(self):
        """ Tests that update should ignore any args past the 4th """
        """ id, size, x, y, (.......) << gets ignored """
        x = Square(10, 10)
        x.update(1, 1, 1, 1, 1, 1)
        self.assertEqual(x.id, 1)
        self.assertEqual(x.size, 1)
        self.assertEqual(x.x, 1)
        self.assertEqual(x.y, 1)

    def test_kwargs_should_be_skipped_if_args_is_not_empty(self):
        """ Checks that any kwargs are skipped if *args is not empty """
        x = Square(5, 5, 5, 5)
        x.update(666, id=555)
        self.assertEqual(x.id, 666)
        x.update(404, 10)
        self.assertEqual(x.size, 10)
        x.update(777, 10, x=20)
        self.assertEqual(x.x, 5)
        x.update(666, y=10)
        self.assertEqual(x.y, 5)

    def test_update_should_set_attributes_if_kwargs_is_not_empty(self):
        """ Checks that the update method updates the attribte from kwargs """
        x = Square(5, 5, 5, 5)
        x.update(size=10)
        self.assertEqual(x.size, 10)
        self.assertEqual(x.id, 5)

        x = Square(5, 5, 5, 5)
        x.update(id=666)
        self.assertEqual(x.id, 666)

        x = Square(9, 7)
        x.update(x=4)
        self.assertEqual(x.x, 4)

    def test_update_order_does_not_matter_with_kwargs(self):
        """ Tests that kwargs can be set in any order"""
        x = Square(10)
        x.update(x=5, size=20, id=666, y=45)
        self.assertEqual(x.x, 5)
        self.assertEqual(x.y, 45)
        self.assertEqual(x.id, 666)
        self.assertEqual(x.size, 20)

    def test_update_does_not_set_foreign_kwargs(self):
        """ Tests that AttributeError is raised with a foreign kwarg """
        x = Square(10, 10)
        x.update(color='red')
        with self.assertRaises(AttributeError):
            self.assertEqual(x.color, 'red')

    def test_dictionary_holds_all_attributes(self):
        """ Test that attributes id, size, x, and y are stored in dict """
        x = Square(6, 7, 9, 10)
        x_dict = x.to_dictionary()
        self.assertEqual('id' in x_dict, True)
        self.assertEqual('size' in x_dict, True)
        self.assertEqual('x' in x_dict, True)
        self.assertEqual('y' in x_dict, True)

        x = Square(6)
        x_dict = x.to_dictionary()
        self.assertEqual('id' in x_dict, True)
        self.assertEqual('size' in x_dict, True)
        self.assertEqual('x' in x_dict, True)
        self.assertEqual('y' in x_dict, True)

    def test_to_dictionary_returns_a_dictionary(self):
        """ Test that to_dictionary method returns a dictionary """
        x = Square(5, 10)
        x_dict = x.to_dictionary()
        self.assertEqual(dict, type(x_dict))
