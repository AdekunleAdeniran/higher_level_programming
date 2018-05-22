#!/usr/bin/python3

""" Base Class TestCases """

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import json
import pep8
import sys
import io
import os


class BaseModelTestCase(unittest.TestCase):
    """ TestCases for Base Model """

    def test_instances_can_have_same_id(self):
        """ Tests that instances can have same id """
        x = Base(1)
        self.assertEqual(x.id, 1)
        y = Base(1)
        self.assertEqual(x.id, y.id)

    def test_base_id_is_1_if_not_set_in_kwarg(self):
        """ Tests that the id attribute is one if no id is set """
        x = Base()
        self.assertEqual(x.id, 1)
        x = Base()
        self.assertEqual(x.id, 2)
        x = Base(10)
        self.assertEqual(x.id, 10)

    def test_base_id_can_be_any_type(self):
        """ Tests that id attribute is set, no matter what type it is """
        x = Base('my_id')
        self.assertEqual(x.id, 'my_id')
        x = Base([1, 2, 3])
        self.assertEqual(x.id, [1, 2, 3])
        x = Base((1,))
        self.assertEqual(x.id, (1,))
        x = Base({'a': 1, 'b': [1, 2]})
        self.assertEqual(x.id, {'a': 1, 'b': [1, 2]})

    def test_base_id_can_be_set_with_a_variable(self):
        """ Tests that id can be set via a variable """
        my_id = 666
        x = Base(my_id)
        self.assertEqual(x.id, 666)
        my_id /= 2
        self.assertEqual(x.id, 666)
        x = Base(my_id)
        self.assertEqual(x.id, 333)

    def test_base_id_can_be_negative_or_0(self):
        """ Tests that id can be <= 0 """
        x = Base(-4)
        self.assertEqual(x.id, -4)
        x = Base(0)
        self.assertEqual(x.id, 0)

    def test_nb_objects_is_private_and_cannot_be_changed_directly(self):
        """ Tests that __nb_object cannot be changed without creating
            a new instance """
        # if it's private it should say Base has no attribute __nb_objects
        with self.assertRaises(AttributeError):
            Base.__nb_objects += 10

    def test_json_string_method_returns_a_string(self):
        """ Tests that to_json_string() return a string """
        x = Base()
        ld = [{'id': 1, 'width': 5, 'height': 10, 'x': 0, 'y': 0}]
        result = x.to_json_string(ld)
        self.assertEqual(type(result), str)

    def test_json_string_method_returns_string_if_arg_is_None(self):
        """ if list_dictionaries is None or empty, return '[]' """
        x = Base()
        list_dictionaries = []
        result = x.to_json_string(list_dictionaries)
        self.assertEqual(result, '[]')

        list_dictionaries = None
        result = x.to_json_string(list_dictionaries)
        self.assertEqual(result, '[]')

        list_dictionaries = [{}]
        result = x.to_json_string(list_dictionaries)
        self.assertEqual(result, '[{}]')

    def test_json_string_method_argument_that_is_not_list_of_dicts(self):
        """ if list_dictionaries isn't a list of dictionaries,
            it should still return a json string """
        x = Base()
        list_dictionaries = [1, 2, 3]
        result = x.to_json_string(list_dictionaries)
        self.assertEqual(result, json.dumps(list_dictionaries))

        list_dictionaries = (1, 2, 3)
        result = x.to_json_string(list_dictionaries)
        self.assertEqual(result, json.dumps(list_dictionaries))

        list_dictionaries = 'hello'
        result = x.to_json_string(list_dictionaries)
        self.assertEqual(result, json.dumps(list_dictionaries))


    def test_json_string_is_None(self):
        """ Tests that from_json_string handles None arg """
        x = Square(10)
        result = x.from_json_string(None)
        self.assertEqual(result, [])

    def test_save_to_file_returns_an_empty_list_if_list_objs_is_none(self):
        """ Tests that save_to_file() returns an empty list if arg is None """
        x = Square(10)
        list_objs = None
        result = x.save_to_file(list_objs)
        self.assertEqual(result, [])

    def test_from_json_string_returns_a_list(self):
        """ Tests that from_json_string() returns a list """
        x = Base()
        test_list = [{'a': 1}, {'b': 2}]
        json_string = json.dumps(test_list)
        result = x.from_json_string(json_string)
        self.assertEqual(type(result), list)

    def test_load_from_file_returns_an_empty_list_if_file_does_not_exist(self):
        """ Tests that [] is returned if .json file doesn't exist """
        x = Base(5)
        # remove Square.json from dir
        result = x.load_from_file()
        self.assertEqual(result, [])

    def test_load_from_file_returns_a_list(self):
        """ Tests that the return value of load_from_file() is a list """
        x = Base()
        result = x.load_from_file()
        self.assertEqual(result, [])

    def test_pep8_module(self):
        '''Test for pep8'''
        pep = pep8.StyleGuide(quiet=True)
        p = pep.check_files(['models/base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_test(self):
        '''Test for pep8'''
        pep = pep8.StyleGuide(quiet=True)
        p = pep.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")
