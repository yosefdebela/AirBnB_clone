#!/usr/bin/python3
import os
import sys
import pycodestyle
import unittest
from models.city import City
from models.base_model import BaseModel
sys.path.append(os.path.abspath(os.path.join
                                (os.path.dirname(__file__), '../../')))


class TestCity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.city1 = City()
        cls.city1.name = "Accra"
        cls.city1.state_id = "GA"

    @classmethod
    def tearDownClass(cls):
        del cls.city1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['../../models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.city1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        self.assertIsNotNone(City.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.city1.__dict__)
        self.assertTrue('created_at' in self.city1.__dict__)
        self.assertTrue('updated_at' in self.city1.__dict__)
        self.assertTrue('state_id' in self.city1.__dict__)
        self.assertTrue('name' in self.city1.__dict__)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.city1.name), str)
        self.assertEqual(type(self.city1.state_id), str)

    def test_save(self):
        self.city1.save()
        self.assertNotEqual(self.city1.created_at, self.city1.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.city1), True)


if __name__ == "__main__":
    unittest.main()
