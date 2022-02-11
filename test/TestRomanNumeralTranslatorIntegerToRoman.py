from unittest import TestCase

from RomanNumeralTranslator import RomanNumeralTranslator


class TestRomanNumeralTranslatorIntegerToRoman(TestCase):
    def test_1_is_I(self):
        self.assertEqual('I', RomanNumeralTranslator.to_roman(1))

    def test_2_is_II(self):
        self.assertEqual('II', RomanNumeralTranslator.to_roman(2))

    def test_3_is_III(self):
        self.assertEqual('III', RomanNumeralTranslator.to_roman(3))

    def test_4_is_IV(self):
        self.assertEqual('IV', RomanNumeralTranslator.to_roman(4))

    def test_5_is_V(self):
        self.assertEqual('V', RomanNumeralTranslator.to_roman(5))

    def test_6_is_VI(self):
        self.assertEqual('VI', RomanNumeralTranslator.to_roman(6))

    def test_9_is_IX(self):
        self.assertEqual('IX', RomanNumeralTranslator.to_roman(9))

    def test_10_is_X(self):
        self.assertEqual('X', RomanNumeralTranslator.to_roman(10))

    def test_11_is_XI(self):
        self.assertEqual('XI', RomanNumeralTranslator.to_roman(11))

    def test_1492_is_MCDXCII(self):
        self.assertEqual('MCDXCII', RomanNumeralTranslator.to_roman(1492))

    def test_6435_is_MMMMMMCDXXXV(self):
        self.assertEqual('MMMMMMCDXXXV', RomanNumeralTranslator.to_roman(6435))

    def test_100000_is_M_hundred_times(self):
        self.assertEqual('M' * 100, RomanNumeralTranslator.to_roman(100000))
