import pytest
import unittest
import coverage

import Julius_McWilliams_hw1


class Tester(unittest.TestCase):
    def test_leap2(self):
        result = Julius_McWilliams_hw1.leap(1978)
        self.assertEqual(result,True)
    def test_leap3(self):
        result = Julius_McWilliams_hw1.leap(2000)
        self.assertEqual(result,False)
    def test_leappt3(self):
        result = Julius_McWilliams_hw1.leap(2100)
        self.assertEqual(result,False)