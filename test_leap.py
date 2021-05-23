import pytest
import unittest
import coverage
import Pytest-cov
import Julius_McWilliams_hw1


class Tester(unittest.TestCase):
    def test_leap1(self):
        result = Julius_McWilliams_hw1.leap("2000")
        self.assertEqual(result,True)
    def test_leap2(self):
        result = Julius_McWilliams_hw1.leap(1978)
        self.assertEqual(result,False)
    def test_leap3(self):
        result = Julius_McWilliams_hw1.leap(2000)
        self.assertEqual(result,True)
    def test_leappt1(self):
        result = Julius_McWilliams_hw1.leap("Johhoj")
        self.assertEqual(result,False)
    def test_leappt2(self):
        result = Julius_McWilliams_hw1.leap(2012)
        self.assertEqual(result,True)
    def test_leappt3(self):
        result = Julius_McWilliams_hw1.leap(2100)
        self.assertEqual(result,False)