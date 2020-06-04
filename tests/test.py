import unittest
import csv
from interpolate_matrix import interpolate_matrix, interpolate_element


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

    # acceptance/integration test
    def test_interpolate_input_test_data_1(self):
        self.assertEqual(interpolate_matrix(
            self.input_test_data_1), self.interpolated_test_data_1)

    # north south east west
    def test_interpolate_none_none_70p807258_59p865848(self):
        self.assertEqual(interpolate_element(None, None, 70.807258, 59.865848), 65.336553)

    """
    15.599452,5.808361,86.617615,60.111501,70.807258
    2.058449,96.990985,nan,21.233911,18.182497
    nan,30.424224,52.475643,43.194502,29.122914

    64.3295385
    """
    def test_interpolate_86p617615_21p233911_52p475643_96p990985(self):
        self.assertEqual(interpolate_element(86.617615, 21.233911, 52.475643, 59.865848), 64.3295385)

    """
    2.058449,96.990985,nan,21.233911,18.182497
    nan,30.424224,52.475643,43.194502,29.122914
    61.185289,13.949386,29.214465,nan,45.606998

    31.222654
    """
    def test_interpolate_2p058449_30p424224_61p185289_None(self):
        self.assertEqual(interpolate_element(2.058449, 30.424224, 61.185289, None), 31.222654)

    """
    nan,30.424224,52.475643,43.194502,29.122914
    61.185289,13.949386,29.214465,nan,45.606998
    """
    def test_interpolate_43p194502_45p606998_None_29p214465(self):
        self.assertEqual(interpolate_element(43.194502, 45.606998, None, 29.214465), 39.338655)

if __name__ == '__main__':
    unittest.main()
