import unittest
import csv
from interpolate_matrix import interpolated_matrix, interpolate_element
from decimal import *

class TestInterpolateMatrix(unittest.TestCase):

    def setUp(self):
        self.input_test_data_1 = []
        with open('./example_data/input_test_data.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                self.input_test_data_1.append(
                    [row[0], row[1], row[2], row[3], row[4]])

        self.interpolated_test_data_1 = []
        with open('./example_data/interpolated_test_data.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                self.interpolated_test_data_1.append(
                    [row[0], row[1], row[2], row[3], row[4]])

        # getcontext().prec = 8

    # acceptance/integration test
    def test_interpolate_input_test_data_1(self):
        self.assertEqual(
            interpolated_matrix(self.input_test_data_1), 
            self.interpolated_test_data_1)

    # north east south west
    """
    given:
    59.865848,  nan
                70.807258

    expect: 65.336553

    >>> mean([70.807258, 59.865848])
    65.33655300000001
    """
    def test_interpolate_none_none_70p807258_59p865848(self):
        self.assertEqual(interpolate_element([None, None, Decimal('70.807258'), Decimal('59.865848')]), Decimal('65.336553'))
    """
    given:
                86.617615
    96.990985,  nan,        21.233911
                52.475643

    expect: 64.3295385

    >>> mean([86.617615, 21.233911, 52.475643, 96.990985])
    64.3295385
    """
    def test_interpolate_86p617615_21p233911_52p475643_96p990985(self):
        self.assertEqual(interpolate_element([Decimal('86.617615'), Decimal('21.233911'), Decimal('52.475643'), Decimal('96.990985')]), Decimal('64.3295385'))

    """
    given:
    2.058449
    nan,        30.424224
    61.185289

    expect: 31.222654

    >>> mean([2.058449, 30.424224, 61.185289])
    31.222654
    """
    def test_interpolate_2p058449_30p424224_61p185289_None(self):
        self.assertEqual(interpolate_element([Decimal('2.058449'), Decimal('30.424224'), Decimal('61.185289'), None]), Decimal('31.222654'))

    """
    given:
                43.194502
    29.214465,  nan,        45.606998

    expect: 39.338655

    >>> mean([43.194502, 45.606998, 29.214465])
    39.338655
    """
    def test_interpolate_43p194502_45p606998_None_29p214465(self):
        self.assertEqual(interpolate_element([Decimal('43.194502'), Decimal('45.606998'), None, Decimal('29.214465')]), Decimal('39.338655'))

if __name__ == '__main__':
    unittest.main()
