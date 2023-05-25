#!/usr/bin/python3
"""
A module that contains the test suite for the BaseModel class
"""
import unittest

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    The test suite for models.base_model.BaseModel
    """

    def test_if_BaseModel_instance_has_id(self):
        """
        Checks that instance has an id assigned on initialization
        """
        b = BaseModel()
        self.assertTrue(hasattr(b, "id"))

if __name__ == "__main__":
    unittest.main()
