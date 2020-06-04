

def interpolate_matrix(matrix):
    pass


def interpolate_element(values):
    available_values = [x for x in values if x is not None]
    # print(f'available_values: {available_values}')
    return round(sum(available_values) / len(available_values), 6)