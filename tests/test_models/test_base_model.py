#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import unittest
import pycodestyle  # ✅ use pycodestyle instead of pep8
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base1 = BaseModel()
        cls.base1.name = "Yosef"
        cls.base1.my_number = 29

    @classmethod
    def tearDownClass(cls):
        del cls.base1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests pycodestyle (PEP8) compliance
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['../../models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "fix pycodestyle issues")

    def test_checking_for_functions(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attributes(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
        self.assertTrue(isinstance(self.base1, BaseModel))

    def test_save(self):
        self.base1.save()
        self.assertNotEqual(self.base1.created_at, self.base1.updated_at)

    def test_to_dict(self):
        base1_dict = self.base1.to_dict()
        self.assertEqual(self.base1.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base1_dict['created_at'], str)
        self.assertIsInstance(base1_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
