import numpy as np

zeros = np.zeros(10)
print(zeros)

fives = np.full(10, 5)
print(fives)

fifty_range = np.arange(10, 51, 1)
print(fifty_range)

nine_range = np.arange(9).reshape(3, 3)
print(nine_range)

eye_matrix = np.eye(3)
print(eye_matrix)

gauss_matrix_size = (5, 5)
gauss_matrix = np.random.normal(size=gauss_matrix_size)
print(gauss_matrix)

ten_matrix = np.arange(0.0, 1.0, 0.01).reshape(10, 10)
print(ten_matrix)

lin_array = np.linspace(0, 1, 20)
print(lin_array)

random_array = np.random.random_integers(1, 25, 25)
first_random_matrix = random_array.reshape((5, 5))
print(first_random_matrix)

sum = first_random_matrix.sum()
print(sum)
mean = first_random_matrix.mean()
print(mean)
deviation = first_random_matrix.std()
print(deviation)
cumsum = first_random_matrix.sum(axis=0)
print(cumsum)

second_random_matrix = np.random.random_integers(0, 100, (5, 5))
print(second_random_matrix)

median = np.median(second_random_matrix)
print(median)
min = np.min(second_random_matrix)
print(min)
max = np.max(second_random_matrix)
print(max)

third_random_matrix = np.random.random_integers(0, 100, (2, 4))
print(third_random_matrix)
transposed = third_random_matrix.transpose()
print(transposed)

first_matrix = np.random.random_integers(0, 15, (3, 4))
second_matrix = np.random.random_integers(0, 15, (3, 4))
sum_matrix = np.add(first_matrix, second_matrix)
print(first_matrix)
print(second_matrix)
print(sum_matrix)

third_matrix = np.random.random_integers(10, 50, (5, 6))
fourth_matrix = np.random.random_integers(10, 50, (6, 5))
print(third_matrix)
print(fourth_matrix)
first_multiply = np.matmul(third_matrix, fourth_matrix)
second_multiply = np.dot(third_matrix, fourth_matrix)
print(first_multiply)
print(second_multiply)