
from statistics import mean

NAN_STRING='nan'

def interpolated_matrix(matrix):
    # assuming matrix is a list of lists of numbers
    # where each list of numbers is a row in the matrix
    if matrix is [[]]:
        return [[]]
    
    h = len(matrix)
    w = len(matrix[0])
    print(f'\nh: {h}, w: {w}')

    for y, row in enumerate(matrix):
        # print(f'i: {i}, row: {row}')
        for x, cell in enumerate(row):
            # print(f'matrix[{y}][{x}]: {cell}')
            if cell == NAN_STRING:
                # North East South West
                interpolated = interpolate_element([
                    float(matrix[y - 1][x]) if y > 0 and matrix[y - 1][x] is not NAN_STRING else None, # N
                    float(matrix[y][x + 1]) if x + 1 <= w - 1 and matrix[y][x + 1] is not NAN_STRING else None, # E
                    float(matrix[y + 1][x]) if y + 1 <= h - 1 and matrix[y + 1][x] is not NAN_STRING else None, # S
                    float(matrix[y][x - 1]) if x - 1 >= 0 and matrix[y][x - 1] is not NAN_STRING else None, # W
                ])
                print(f'interpolated: {interpolated}\n')
                # print(f'round(interpolated, 6): {round(interpolated, 6)}')
                # matrix[y][x] = str(round(interpolated, 6))
                matrix[y][x] = str(interpolated)
                # FIXME or, replace all NAN_STRING with None?
                # so can do e.g. matrix[x, y - 1] if y > 0, # N
    # print(matrix)
    return matrix

def interpolate_element(values):
    non_none_values = [x for x in values if x is not None]
    print(f'values: {values}')
    print(f'non_none_values: {non_none_values}')
    # return round(sum(available_values) / len(available_values), 6)
    # return mean(non_none_values)
    print(f'round(mean(non_none_values), 10): {round(mean(non_none_values), 10)}')
    return round(mean(non_none_values), 10)
