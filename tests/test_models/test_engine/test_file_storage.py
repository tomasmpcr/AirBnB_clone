#!/usr/bin/python3
#Import moduls
import unittest
from models.engine.file_storage import FileStorage
import pep8

#================================================================================
# https://pep8.readthedocs.io/en/release-1.7.x/advanced.html

class pep8_test(unittest.TestCase):
    """pep8 test cases class"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style Werrors (and warnings).")


class docs_test(unittest.TestCase):
    """Base model document tests"""

    def test_module_docstring(self):
        """module doc"""
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def test_class_docstring(self):
        """class doc"""
        self.assertTrue(len(FileStorage.__doc__) >= 1)

if __name__ == "__main__":
    unittest.main()
