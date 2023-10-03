import unittest
import os
import random
import string
import functions

class TestFunctions(unittest.TestCase):

    def test_urlclean(self):
        self.assertEqual(functions.cleanurl('web.com/'),'https://web.com/api')
