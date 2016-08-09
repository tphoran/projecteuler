
import numpy as np


class Eleven(object):
    """
    In the 20 by 20 grid below, four numbers along a diagonal line have been marked in red.

    The product of these numbers is 26 * 63 * 78 * 14 = 1788696.

    What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally)
    in the 20 by 20 grid?
    """

    def __init__(self, adjacent_number_count, matrix):
        self.adjacent_number_count = adjacent_number_count
        self.matrix = matrix

    def calculate_high_product_vertically_in_matrix(self, matrix):
        max_product_vertically_in_matrix = max(matrix.prod(axis=0).tolist()[0])
        return max_product_vertically_in_matrix

    def calculate_top_left_to_bottom_right_diagonal_product_in_matrix(self, matrix):
        top_left_to_bottom_right_list = matrix.diagonal(offset=0, axis1=0, axis2=1).tolist()[0]
        max_product_of_top_left_to_bottom_right_list = 1
        for i in top_left_to_bottom_right_list:
            max_product_of_top_left_to_bottom_right_list *= i
        return max_product_of_top_left_to_bottom_right_list

    def rotate_matrix_90_degrees(self, matrix):
        rotated_matrix = matrix.transpose()
        return rotated_matrix

    def create_list_of_x_by_x_sized_matrixes(self, x_by_x, original_matrix):
        width_of_matrix, height_of_matrix = original_matrix.shape
        list_of_matrixes = []
        for x in range(height_of_matrix + 1 - x_by_x):
            for y in range(width_of_matrix + 1 - x_by_x):
                temp_right_sized_matrix = original_matrix[y:y + x_by_x, x:x + x_by_x]
                list_of_matrixes.append(temp_right_sized_matrix)
        return list_of_matrixes

    def hightest_product_of_x_numbers_in_matrix_vertically(self, adjacent_number_count, matrix):
        highest_product_of_x_number_in_matrix_vertically = None
        list_of_x_by_x_matrixes = self.create_list_of_x_by_x_sized_matrixes(adjacent_number_count, matrix)
        for i in list_of_x_by_x_matrixes:
            temp_max_product_vertically = self.calculate_high_product_vertically_in_matrix(i)
            if temp_max_product_vertically > highest_product_of_x_number_in_matrix_vertically:
                highest_product_of_x_number_in_matrix_vertically = temp_max_product_vertically
        return highest_product_of_x_number_in_matrix_vertically

    def highest_product_of_x_numbers_in_matrix_diagonally(self, adjacent_number_count, matrix):
        highest_product_of_x_number_in_matrix_diagonally = None
        list_of_x_by_x_matrixes = self.create_list_of_x_by_x_sized_matrixes(adjacent_number_count, matrix)
        for i in list_of_x_by_x_matrixes:
            temp_diagonal_product = self.calculate_top_left_to_bottom_right_diagonal_product_in_matrix(i)
            if temp_diagonal_product > highest_product_of_x_number_in_matrix_diagonally:
                highest_product_of_x_number_in_matrix_diagonally = temp_diagonal_product
        return highest_product_of_x_number_in_matrix_diagonally

    def solve(self):
        rotated_matrix = self.rotate_matrix_90_degrees(self.matrix)

        highest_vertical_product = self.hightest_product_of_x_numbers_in_matrix_vertically(self.adjacent_number_count,
                                                                                           self.matrix)
        highest_horizontal_product = self.hightest_product_of_x_numbers_in_matrix_vertically(self.adjacent_number_count,
                                                                                             rotated_matrix)
        highest_diagonal_product = self.highest_product_of_x_numbers_in_matrix_diagonally(self.adjacent_number_count,
                                                                                          self.matrix)
        highest_diagonal_product_rotated = self.highest_product_of_x_numbers_in_matrix_diagonally(self.adjacent_number_count,
                                                                                                  rotated_matrix)

        return max(highest_vertical_product, highest_horizontal_product, highest_diagonal_product,
                   highest_diagonal_product_rotated)








test_matrix = np.matrix('0 1 2 3 4; 0 1 2 3 4; 0 1 2 3 4; 0 1 2 3 4')

test_eleven = Eleven(3, test_matrix)

test_eleven.hightest_product_of_x_numbers_in_matrix_vertically(3, test_matrix)

rotated_matrix = test_eleven.rotate_matrix_90_degrees(test_matrix)

print test_matrix
print rotated_matrix

temp_matrix = test_matrix[0:3,2:5]
print test_matrix
print rotated_matrix



test_matrix = np.matrix('0 5 0 1; 0 0 1 5; 0 1 0 0; 1 0 0 0')

array_diag = test_matrix.diagonal(offset=0, axis1=0, axis2=1).tolist()[0]

array_diag_2 = test_matrix.diagonal(offset=0, axis1=1, axis2=0).tolist()[0]

print array_diag
print array_diag_2

print test_matrix
test_matrix_2 = test_matrix.transpose().transpose()
print test_matrix_2


test_matrix_2 = test_matrix[0:2,0:2]

print test_matrix
print test_matrix_2

print test_matrix[0].tolist()[0][0]
print test_matrix.shape[1]
width_of_matrix, height_of_matrix = test_matrix.shape
print width_of_matrix

print test_matrix.cumprod(axis = 0)[3:3]
print test_matrix.cumprod(axis = 1)

for i in test_matrix.cumprod(axis = 0):
    print max(max(i.tolist()))
