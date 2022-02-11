from unittest import TestCase

from RomanNumeralTranslator import RomanNumeralTranslator


class TestRomanNumeralTranslatorRomanToInteger(TestCase):
    def test_I_is_1(self):
        self.assertEqual(1, RomanNumeralTranslator.to_int('I'))

    def test_II_is_2(self):
        self.assertEqual(2, RomanNumeralTranslator.to_int('II'))

    def test_III_is_3(self):
        self.assertEqual(3, RomanNumeralTranslator.to_int('III'))

    def test_IV_is_4(self):
        self.assertEqual(4, RomanNumeralTranslator.to_int('IV'))

    def test_V_is_5(self):
        self.assertEqual(5, RomanNumeralTranslator.to_int('V'))

    def test_VI_is_6(self):
        self.assertEqual(6, RomanNumeralTranslator.to_int('VI'))

    def test_VII_is_7(self):
        self.assertEqual(7, RomanNumeralTranslator.to_int('VII'))

    def test_VIII_is_8(self):
        self.assertEqual(8, RomanNumeralTranslator.to_int('VIII'))

    def test_IX_is_9(self):
        self.assertEqual(9, RomanNumeralTranslator.to_int('IX'))

    def test_X_is_10(self):
        self.assertEqual(10, RomanNumeralTranslator.to_int('X'))

    def test_XI_is_11(self):
        self.assertEqual(11, RomanNumeralTranslator.to_int('XI'))

    def test_XIV_is_14(self):
        self.assertEqual(14, RomanNumeralTranslator.to_int('XIV'))

    def test_XIX_is_19(self):
        self.assertEqual(19, RomanNumeralTranslator.to_int('XIX'))

    def test_XX_is_20(self):
        self.assertEqual(20, RomanNumeralTranslator.to_int('XX'))

    def test_LIV_is_54(self):
        self.assertEqual(54, RomanNumeralTranslator.to_int('LIV'))

    def test_MCDXCII_is_1492(self):
        self.assertEqual(1492, RomanNumeralTranslator.to_roman('MCDXCII'))

    def test_MMMMMMCDXXXV_is_6435(self):
        self.assertEqual(6435, RomanNumeralTranslator.to_roman('MMMMMMCDXXXV'))

    def test_M_hundred_times_is_100000(self):
        self.assertEqual(100000, RomanNumeralTranslator.to_roman('M' * 100))
