import numpy as np


def calculate_scaling_constant(vector):
    # print("max element is ",vector.max())
    return float(1 / vector.max())

def calculate_authority(transposed_matrix, hub_vector):
    # print("DEBUG: ")
    # print(transposed_matrix)
    # print(hub_vector)
    multiplication = transposed_matrix.dot(hub_vector)
    # print("L^T * h is: ")
    # print(multiplication)
    μ = calculate_scaling_constant(multiplication)
    # print("μ == ", μ)
    return multiplication * (μ)

def calculate_hubiness(matrix):
    λ = calculate_scaling_constant(matrix)
    # print("λ == ", λ)
    return matrix * (λ)


# !!!! INIT PHASE !!!! #

matrix = np.array([[0, 1, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0],
                   [0, 1, 0, 0, 0, 0],
                   [0, 0, 0, 1, 0, 1],
                   [0, 0, 0, 0, 0, 0]])

hub_vector = np.array([1, 1, 1, 1, 1, 1])
nodes = ["A", "B", "C", "D", "E", "F"]
count_of_nodes = 6

# MATRIX FROM THE 4th LESSON:
# matrix = np.array([[0, 1, 1, 1, 0],
#                    [1, 0, 0, 1, 0],
#                    [0, 0, 0, 0, 1],
#                    [0, 1, 1, 0, 0],
#                    [0, 0, 0, 0, 0]])

# !!!! ALGORITHM PART !!!! #

transposed_matrix = matrix.transpose()
authority_vector = np.array([])
intermediate_matrix = matrix


iterations = int(input("Enter count of iterations: "))
for i in range(1, iterations + 1):
    print("ITERATION №", i)
    # print("L^T is: ")
    # print(transposed_matrix)
    authority_vector = calculate_authority(transposed_matrix, hub_vector)
    # print("AUTHORITY VECTOR: ")
    # print(authority_vector)
    intermediate_matrix = matrix.dot(authority_vector)
    # print("L * a is: ")
    # print(intermediate_matrix)
    hub_vector = calculate_hubiness(intermediate_matrix)
    # print("HUB VECTOR: ")
    # print(hub_vector)
    print("Node:     Authority:         Hubbiness:")
    for i in range(0, count_of_nodes):
        print(nodes[i], "       ", "%.10f" %authority_vector[i], "     ", "%.10f" %hub_vector[i])