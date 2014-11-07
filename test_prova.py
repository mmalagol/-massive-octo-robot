from unittest import TestCase
from Prova import Prova

__author__ = 'matteo.malagoli'


class TestProva(TestCase):
    def test_conta(self):
        self.fail()
    def test_conta(self):
        p = Prova
        self.assertRaises(Exception,p.conta,'pluto')