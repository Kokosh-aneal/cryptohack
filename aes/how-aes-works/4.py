state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    flattened_matrix = [item for row in matrix for item in row]
    result_bytes = bytes(flattened_matrix)
    return result_bytes

def add_round_key(s, k):
    """ XORs each element of the state matrix with the corresponding element of the round key matrix. """
    # Ensure the matrices have the same dimensions
    if len(state) != len(round_key) or any(len(state[i]) != len(round_key[i]) for i in range(len(state))):
        raise ValueError("Matrices must have the same dimensions")

    # Create a new matrix to store the result
    result_matrix = [[state[i][j] ^ round_key[i][j] for j in range(len(state[i]))] for i in range(len(state))]

    return result_matrix
    


print(add_round_key(state, round_key))
print(matrix2bytes(add_round_key(state,round_key)))

