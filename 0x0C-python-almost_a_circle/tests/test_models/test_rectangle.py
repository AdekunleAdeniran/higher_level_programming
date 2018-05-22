#!/usr/bin/python3

""" Rectangle Class TestCases """

from models.rectangle import Rectangle
from models.base import Base
import unittest
import sys          # for stdout access
import io           # for stdout printing tests


class RectangleModelTestCase(unittest.TestCase):
    """ TestCases for Rectangle Model
        Rectangle(width, height, x, y, id) """

    def test_that_Rectangle_inherits_from_Base(self):
        """ Tests that Rectangle inherits from Base """
        x = Rectangle(10, 10)
        self.assertEqual(issubclass(Rectangle, Base), True)

    def test_Rectangle_inherits_id_from_Base(self):
        """ Tests that id is inherited from base, it should never be None """
        x = Rectangle(10, 10)
        self.assertEqual(x.id is None, False)
        x = Rectangle(10, 10, id=None)
        self.assertEqual(x.id is None, False)

    def test_if_width_is_int(self):
        """ Checks if width is an int """
        x = Rectangle(10, 10)
        self.assertEqual(type(x.width), int)

    def test_width_can_be_very_big(self):
        """ Checks that width can be max int """
        x = Rectangle(sys.maxsize, 5)
        self.assertEqual(x.width, sys.maxsize)

    def test_raise_TypeError_if_width_is_not_int(self):
        """ Checks for TypeError exception if width is not an int """
        with self.assertRaises(TypeError):
            x = Rectangle('a string', 10)

        exc_msg = 'width must be an integer'
        with self.assertRaises(TypeError) as msg:
            x = Rectangle({}, 10)
        self.assertEqual(str(msg.exception), exc_msg)

        with self.assertRaises(TypeError) as msg:
            x = Rectangle([4], 10)
        self.assertEqual(str(msg.exception), exc_msg)

        with self.assertRaises(TypeError) as msg:
            x = Rectangle((1,), 10)
        self.assertEqual(str(msg.exception), exc_msg)

        with self.assertRaises(TypeError) as msg:
            x = Rectangle({1: 'a', 2: 'b'}, 10)
        self.assertEqual(str(msg.exception), exc_msg)

    def test_if_height_is_int(self):
        """ Checks if height is an int """
        x = Rectangle(10, 10)
        self.assertEqual(type(x.height), int)

    def test_height_can_be_very_big(self):
        """ Checks that height can be max int """
        x = Rectangle(10, sys.maxsize)
        self.assertEqual(x.height, sys.maxsize)

    def test_raise_TypeError_if_height_is_not_int(self):
        """ Checks if TypeError message meets specs """
        exc_msg = 'height must be an integer'
        with self.assertRaises(TypeError) as msg:
            x = Rectangle(10, [1, 4])
        self.assertEqual(str(msg.exception), exc_msg)

        with self.assertRaises(TypeError) as msg:
            x = Rectangle(10, (1,))
        self.assertEqual(str(msg.exception), exc_msg)

        with self.assertRaises(TypeError) as msg:
            x = Rectangle(10, {'x': None})
        self.assertEqual(str(msg.exception), exc_msg)

    def test_raise_ValueError_if_width_is_less_than_zero(self):
        """ Checks if width is greater than 0 """
        exc_msg = 'width must be > 0'
        with self.assertRaises(ValueError) as msg:
            x = Rectangle(-9, 10, 4)
        self.assertEqual(str(msg.exception), exc_msg)

        with self.assertRaises(ValueError) as msg:
            x = Rectangle(-23, 10, 4)
        self.assertEqual(str(msg.exception), exc_msg)

    def test_raise_ValueError_if_height_is_less_than_zero(self):
        """ Checks if height is greater than 0 """
        exc_msg = 'height must be > 0'
        with self.assertRaises(ValueError) as msg:
            x = Rectangle(9, -110, 4)
        self.assertEqual(str(msg.exception), exc_msg)

    def test_raise_ValueError_if_x_is_negative(self):
        """ Checks that ValueError is raised if x < 0 """
        exc_msg = 'x must be >= 0'
        with self.assertRaises(ValueError) as msg:
            x = Rectangle(10, 20, -1, 1)
        self.assertEqual(str(msg.exception), exc_msg)

    def test_raise_ValueError_if_y_is_negative(self):
        """ Checks that ValueError is raised if y < 0 """
        exc_msg = 'y must be >= 0'
        with self.assertRaises(ValueError) as msg:
            x = Rectangle(10, 20, 1, -1)
        self.assertEqual(str(msg.exception), exc_msg)

    def test_x_can_be_very_big(self):
        """ Checks that x can be max int """
        x = Rectangle(10, 10, sys.maxsize)
        self.assertEqual(x.x, sys.maxsize)

    def test_y_can_be_very_big(self):
        """ Checks that y can be max int """
        x = Rectangle(10, 10, 5, sys.maxsize)
        self.assertEqual(x.y, sys.maxsize)

    def test_area_method_returns_correct_value(self):
        """ Checks that area() returns width * height """
        x = Rectangle(2, 6)
        self.assertEqual(x.area(), 12)
        x = Rectangle(1, 1, 80, 98, 0)
        self.assertEqual(x.area(), 1)

    def test_area_method_returns_really_big_number(self):
        """ Checks that area() works with maxsize int """
        x = Rectangle(sys.maxsize, 2)
        self.assertEqual(x.area(), sys.maxsize * 2)

    def test_display_prints_a_rectangle(self):
        """ Checks that the display() method prints a Rectangle """
        x = Rectangle(2, 2)
        output = io.StringIO()  # sets output to an io stream
        sys.stdout = output     # connects the stream to stdout file object
        x.display()
        sys.stdout = sys.__stdout__     # makes file object the sysytems stdout
        self.assertEqual('##\n##\n', output.getvalue())

        x = Rectangle(4, 2)
        output = io.StringIO()
        sys.stdout = output
        x.display()
        sys.stdout = sys.__stdout__
        self.assertEqual('####\n####\n', output.getvalue())

    def test_display_prints_a_rectangle_with_coordinates(self):
        """ Checks that the display() method prints a Rectangle """
        x = Rectangle(2, 2, 1, 1)
        output = io.StringIO()
        sys.stdout = output
        x.display()
        sys.stdout = sys.__stdout__
        self.assertEqual('\n ##\n ##\n', output.getvalue())

        x = Rectangle(2, 2, 3, 1)
        output = io.StringIO()
        sys.stdout = output
        x.display()
        sys.stdout = sys.__stdout__
        self.assertEqual('\n   ##\n   ##\n', output.getvalue())

        x = Rectangle(2, 2, 3)
        output = io.StringIO()
        sys.stdout = output
        x.display()
        sys.stdout = sys.__stdout__
        self.assertEqual('   ##\n   ##\n', output.getvalue())

        x = Rectangle(2, 2, y=3)
        output = io.StringIO()
        sys.stdout = output
        x.display()
        sys.stdout = sys.__stdout__
        self.assertEqual('\n\n\n##\n##\n', output.getvalue())

    def test_str_method_returns_proper_representation(self):
        """ Checks that __str__ is overwritten with specs representation """
        x = Rectangle(4, 6, 2, 1, 12)
        target = '[Rectangle] ({}) {}/{} - {}/{}'.format(
                x.id, x.x, x.y, x.width, x.height)
        self.assertEqual(str(x), target)

        x = Rectangle(10, 50)
        target = '[Rectangle] ({}) {}/{} - {}/{}'.format(
                x.id, x.x, x.y, x.width, x.height)
        self.assertEqual(str(x), target)

    def test_update_args_get_set_correctly(self):
        """ Checks that the update() method updates the correct attributes.
            The order should be: id, width, height, x, y """
        x = Rectangle(10, 10, 10, 10, 10)
        x.update(40, 20)
        self.assertEqual(x.id, 40)
        self.assertEqual(x.width, 20)

        x = Rectangle(5, 5, 5, 5, 5)
        x.update(666)
        self.assertEqual(x.id, 666)
        self.assertEqual(x.width, 5)

        x = Rectangle(1, 1)
        x.update(6, 10)
        self.assertEqual(x.id, 6)
        self.assertEqual(x.width, 10)
        self.assertEqual(x.height, 1)

        x = Rectangle(1, 1)
        x.update(6, 10, 4, 0)
        self.assertEqual(x.id, 6)
        self.assertEqual(x.width, 10)
        self.assertEqual(x.height, 4)
        self.assertEqual(x.y, 0)

    def test_update_with_no_args(self):
        """ Tests that update should do nothing if there are no arguments """
        x = Rectangle(10, 10)
        x.update()
        self.assertEqual(x.width, 10)
        self.assertEqual(x.height, 10)
        self.assertEqual(x.x, 0)
        self.assertEqual(x.y, 0)

    def test_update_with_one_arg(self):
        """ Tests that update should update id if there is one argument """
        x = Rectangle(10, 10)
        x.update(666)
        self.assertEqual(x.width, 10)
        self.assertEqual(x.height, 10)
        self.assertEqual(x.x, 0)
        self.assertEqual(x.y, 0)
        self.assertEqual(x.id, 666)

    def test_update_with_two_args(self):
        """ Tests that update should update id and width
            if there are two arguments """
        x = Rectangle(10, 10)
        x.update(5, 5)
        self.assertEqual(x.width, 5)
        self.assertEqual(x.height, 10)
        self.assertEqual(x.x, 0)
        self.assertEqual(x.y, 0)
        self.assertEqual(x.id, 5)

    def test_update_with_three_args(self):
        """ Tests that update should update id, width, and height
            if there are three arguments """
        x = Rectangle(10, 10)
        x.update(5, 5, 5)
        self.assertEqual(x.width, 5)
        self.assertEqual(x.height, 5)
        self.assertEqual(x.x, 0)
        self.assertEqual(x.y, 0)
        self.assertEqual(x.id, 5)

    def test_update_with_four_args(self):
        """ Tests that update should update id, width, height, and x
            if there are four arguments """
        x = Rectangle(10, 10)
        x.update(5, 5, 5, 5)
        self.assertEqual(x.width, 5)
        self.assertEqual(x.height, 5)
        self.assertEqual(x.x, 5)
        self.assertEqual(x.y, 0)
        self.assertEqual(x.id, 5)

    def test_update_with_five_args(self):
        """ Tests that update should update id, width, height, and x
            if there are five arguments """
        x = Rectangle(10, 10)
        x.update(5, 5, 5, 5, 5)
        self.assertEqual(x.width, 5)
        self.assertEqual(x.height, 5)
        self.assertEqual(x.x, 5)
        self.assertEqual(x.y, 5)
        self.assertEqual(x.id, 5)

    def test_update_with_more_than_5_args(self):
        """ Tests that update should ignore any args past the 5th """
        """ id, width, height, x, y, (.......) << gets ignored """
        x = Rectangle(10, 10)
        x.update(1, 1, 1, 1, 1, 1)
        self.assertEqual(x.id, 1)
        self.assertEqual(x.width, 1)
        self.assertEqual(x.height, 1)
        self.assertEqual(x.x, 1)
        self.assertEqual(x.y, 1)

    def test_kwargs_should_be_skipped_if_args_is_not_empty(self):
        """ Checks that any kwargs are skipped if *args is not empty """
        x = Rectangle(5, 5, 5, 5, 5)
        x.update(666, id=555)
        self.assertEqual(x.id, 666)
        x.update(404, 10)
        self.assertEqual(x.width, 10)
        x.update(777, 10, width=20)
        self.assertEqual(x.width, 10)
        x.update(666, x=10)
        self.assertEqual(x.x, 5)

    def test_update_should_set_attributes_if_kwargs_is_not_empty(self):
        """ Checks that the update method updates the attribte from kwargs """
        x = Rectangle(5, 5, 5, 5, 5)
        x.update(height=10)
        self.assertEqual(x.height, 10)

        x = Rectangle(5, 5, 5, 5, 5)
        x.update(id=666)
        self.assertEqual(x.id, 666)

        x = Rectangle(9, 7)
        x.update(x=4)
        self.assertEqual(x.x, 4)

    def test_update_order_does_not_matter_with_kwargs(self):
        """ Tests that kwargs can be set in any order"""
        x = Rectangle(10, 10)
        x.update(x=5, height=20, id=666, width=30, y=45)
        self.assertEqual(x.x, 5)
        self.assertEqual(x.y, 45)
        self.assertEqual(x.id, 666)
        self.assertEqual(x.width, 30)
        self.assertEqual(x.height, 20)

    def test_update_does_not_set_foreign_kwargs(self):
        """ Tests that AttributeError is raised with a foreign kwarg """
        x = Rectangle(10, 10)
        x.update(color='red')
        with self.assertRaises(AttributeError):
            self.assertEqual(x.color, 'red')

    def test_dictionary_contains_all_attributes(self):
        """ Tests that to_dictionary stores all attributes:
            id, width, height, x, and y """
        x = Rectangle(1, 2, 3, 4, 5)
        x_dict = x.to_dictionary()
        self.assertEqual('id' in x_dict, True)
        self.assertEqual('width' in x_dict, True)
        self.assertEqual('height' in x_dict, True)
        self.assertEqual('x' in x_dict, True)
        self.assertEqual('y' in x_dict, True)
        self.assertEqual(len(x_dict.keys()), 5)

        x = Rectangle(1, 2)
        x_dict = x.to_dictionary()
        self.assertEqual('id' in x_dict, True)
        self.assertEqual('width' in x_dict, True)
        self.assertEqual('height' in x_dict, True)
        self.assertEqual('x' in x_dict, True)
        self.assertEqual('y' in x_dict, True)
        self.assertEqual(len(x_dict.keys()), 5)

    def test_x_is_an_int(self):
        """ Tests that x is an int """
        temp = Rectangle(3, 3, 'x', 4)
        self.assertEqual(temp.x, 0)

    def test_to_dictionary_returns_a_dictionary(self):
        """ Test that to_dictionary method returns a dictionary """
        x = Rectangle(5, 10)
        x_dict = x.to_dictionary()
        self.assertEqual(dict, type(x_dict))
