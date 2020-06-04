import unittest
import csv
from interpolate_matrix import interpolate_matrix

class TestInterpolateMatrix(unittest.TestCase):

    def setUp(self):
        self.input_test_data_1 = []
        with open('./example_data/input_test_data.csv') as f:
          reader = csv.reader(f)
          for row in reader:
            self.input_test_data_1.append([row[0], row[1], row[2], row[3], row[4]])

        self.interpolated_test_data_1 = []
        with open('./example_data/interpolated_test_data.csv') as f:
          reader = csv.reader(f)
          for row in reader:
            self.interpolated_test_data_1.append([row[0], row[1], row[2], row[3], row[4]])

    def test_interpolate_input_test_data_1(self):
        self.assertEqual(interpolate_matrix(self.input_test_data_1), self.interpolated_test_data_1)

if __name__ == '__main__':
    unittest.main()
