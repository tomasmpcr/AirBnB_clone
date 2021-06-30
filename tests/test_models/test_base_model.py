#!/usr/bin/python3
#Import moduls
import unittest
from models.base_model import BaseModel
import pep8
from datetime import datetime
import inspect
import json


#================================================================================
# https://pep8.readthedocs.io/en/release-1.7.x/advanced.html

class pep8_test(unittest.TestCase):
    """pep8 test cases class"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style Werrors (and warnings).")


class docs_test(unittest.TestCase):
    """Base model document tests"""

    def test_module_docstring(self):
        """module doc"""
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_class_docstring(self):
        """class doc"""
        self.assertTrue(len(BaseModel.__doc__) >= 1)


class base_model_test(unittest.TestCase):
    """ Base model test """
    def att_test(self):
        """ att test """
        obj = BaseModel()
        obj2 = BaseModel()
        
        self.assertIsInstance(obj.id, str)
        self.assertNotEqual(obj.id, obj2.id)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertTrue(type(obj), object)
        self.assertTrue(isinstance(obj, BaseModel))

    def base_model_none_test(self):
        """ Base model none test """
        obj = BaseModel(None)
        self.assertNotIn(None, obj.__dict__.values())

    def file_test(self):
        """ file json test """
        obj = BaseModel()
        obj.save()
        obj = "BaseModel." + obj.id
        with open("file.json", "r") as f:
            self.assertIn(obj, f.read())

    def to_dict_test(self):
        """ dict test """
        obj = BaseModel()
        dictionary_5 = obj.to_dict()
        self.assertIsInstance(dictionary_5, dict)
        self.assertEqual(obj.to_dict()["id"], obj.id)
        self.assertEqual(obj.to_dict()["__class__"], "BaseModel")
        obj.save()
        dict_2 = obj.to_dict()
        self.assertNotEqual(dictionary_5["updated_at"], dict_2["updated_at"])

if __name__ == "__main__":
    unittest.main()
