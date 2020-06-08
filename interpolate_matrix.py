
from statistics import mean
from decimal import *

NAN_STRING='nan'

def interpolated_matrix(matrix):
    # assuming matrix is a list of lists of strings representing floating point numbers
    # where each list of strings is a row in the matrix
    if matrix is [[]]:
        return [[]]
    
    h = len(matrix)
    w = len(matrix[0])
    # print(f'\nh: {h}, w: {w}')
    # getcontext().prec = 8

    for y, row in enumerate(matrix):
        for x, cell in enumerate(row):
            if cell == NAN_STRING:
                # North East South West
                interpolated = interpolate_element([
                    Decimal(matrix[y - 1][x]) if y > 0 and matrix[y - 1][x] is not NAN_STRING else None, # N
                    Decimal(matrix[y][x + 1]) if x + 1 <= w - 1 and matrix[y][x + 1] is not NAN_STRING else None, # E
                    Decimal(matrix[y + 1][x]) if y + 1 <= h - 1 and matrix[y + 1][x] is not NAN_STRING else None, # S
                    Decimal(matrix[y][x - 1]) if x - 1 >= 0 and matrix[y][x - 1] is not NAN_STRING else None, # W
                ])
                matrix[y][x] = str(interpolated)
    return matrix

def interpolate_element(values):
    non_none_values = [x for x in values if x is not None]
    return mean(non_none_values)
