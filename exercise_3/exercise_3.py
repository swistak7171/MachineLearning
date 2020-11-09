import numpy as np
from scipy import sparse as sp, linalg as la
import pandas as pd

counter = 1


def separate():
    global counter
    print(f"=================== {counter} ===================")
    counter = counter + 1


# Python Basics
separate()
characters = ['a', 'b', 'c', 'd', 'e', 'b', 'b', 'c']
a_index = characters.index('a')
print(f"Index of 'a' = {a_index}")

separate()
b_count = characters.count('b')
print(f"Count of 'b' = {b_count}")

separate()
characters.sort()
print(f"Sorted list = {characters}")

separate()
characters.reverse()
print(f"Reversed list = {characters}")

separate()
example_string = 'this is example string'
example_string = example_string.upper()
print(f"Uppercase string: {example_string}")


# NumPy Basics

separate()
np_array = np.array([5, 2, 1, 6, 2, 8, 2, 3])
array_sum = np_array.sum()
print(f"Array sum = {array_sum}")

separate()
min_value = np_array.min()
print(f"Min value = {min_value}")

separate()
array_mean = np_array.mean()
print(f"Mean value = {array_mean}")

separate()
second_array = np.array([1, 1, 1, 2, 2, 2, 3, 3])
sum_array = np.add(np_array, second_array)
print(f"Sum array = {sum_array}")

separate()
sqrt_root = np.sqrt(np_array)
print(f"Square root = {sqrt_root}")


# SciPy - Linear Algebra

separate()
matrix = np.asmatrix((np.random.random((3, 3))))
print(f"Matrix = {matrix}")

separate()
inversed_matrix = matrix.I
print(f"Inversed matrix = {inversed_matrix}")

separate()
transposed_matrix = matrix.T
print(f"Transposed matrix = {transposed_matrix}")

separate()
determinant = la.det(matrix)
print(f"Matrix determinant = {determinant}")

separate()
norm = la.norm(matrix)
print(f"Norm = {norm}")


# Pandas Basics

data = {'Country': ['Belgium', 'India', 'Brazil'],
        'Capital': ['Brussels', 'New Delhi', 'Brasília'],
        'Population': [11190846, 1303171035, 207847528]}
data_frame = pd.DataFrame(data)
print(data_frame)

separate()
sorted_data_frame = data_frame.sort_values(by='Population')
print(f"Sorted by population: {sorted_data_frame}")

separate()
(x, y) = data_frame.shape
print(f"Shape: X = {x}, Y = {y}")

separate()
sum_data_frame = data_frame.sum()
print(f"Sum DataFrame = {sum_data_frame}")

separate()
description = data_frame.describe()
print(f"Description: {description}")

separate()
func = lambda x: len(x)
new_frame = data_frame.apply(func)
print(f"Applied function: {new_frame}")


# Scikit-Learn

