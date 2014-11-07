from unittest import TestCase
from Solver import Solver

__author__ = 'matteo.malagoli'


class TestSolver(TestCase):

    def test_negative_discr(self):
      s = Solver
      self.assertRaises(Exception,s.demo,2,1,2)

    def test_demo(self):
        self.fail()

    def test_negative_discr2(self):
      s = Solver
      self.assertRaises(Exception,s.demo,6,1,-9)