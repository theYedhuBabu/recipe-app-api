"""
Sample Tests
"""

from django.test import SimpleTestCase # type: ignore

from app import calc  # type: ignore


class CalcTests(SimpleTestCase):
    def test_add_numbers(self):

        res = calc.add(5, 6)

        self.assertEqual(res, 11)
