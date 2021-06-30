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

    @classmethod
    def setUpClass(cls):
        """Testing class"""
        cls.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_module_docstring(self):
        """module doc"""
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_class_docstring(self):
        """class doc"""
        self.assertTrue(len(BaseModel.__doc__) >= 1)

if __name__ == "__main__":
    unittest.main()
