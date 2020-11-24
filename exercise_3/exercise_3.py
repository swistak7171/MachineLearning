import numpy as np
from bokeh.models import Legend
from scipy import sparse as sp, linalg as la
import pandas as pd
from sklearn import neighbors, datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.svm import SVC
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.plotting import figure
from bokeh.io import output_file, show, save

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

X = np.random.random((10, 5))
y = np.array(['M', 'M', 'F', 'F', 'M', 'F', 'M', 'M', 'F', 'F'])
X[X < 0.7] = 0
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
linear_regression = LinearRegression(normalize=True)
k_means = KMeans(n_clusters=3, random_state=0)
knn = neighbors.KNeighborsClassifier(n_neighbors=5)
svc = SVC(kernel='linear')
pca = PCA(n_components=0.95)

separate()
linear_regression.fit(X, y)
knn.fit(X_train, y_train)
svc.fit(X_train, y_train)

separate()
k_means.fit(X_train)

separate()
pca_model = pca.fit_transform(X_train)

separate()
knn.score(X_test, y_test)


# Matplotlib

x = np.linspace(0, 10, 100)
y = np.cos(x)
z = np.sin(x)

separate()
plot_figure = plt.figure()
axes = plot_figure.add_subplot(111)
axes.plot(x, y)

separate()
axes.scatter([1, 2, 3], [4, 5, 6], marker='*')

separate()
plt.title('Cosinus')

separate()
plt.savefig('plot.png')

separate()
plt.show()


# Seaborn

titanic = sns.load_dataset("titanic")
sns.set_style('ticks')

separate()
sns.countplot(x="deck", data=titanic)
plt.show()

separate()
sns.barplot(x="sex", y="survived", hue="class", data=titanic)
plt.show()

separate()
sns.pointplot(
    x="class",
    y="survived",
    hue="sex",
    data=titanic,
    palette={ "male": "g",
              "female": "m"},
    markers=["^", "o"],
    linestyles=["-", "--"]
)
plt.show()

separate()
sns.violinplot(x="age", y="sex", hue="survived", data=titanic)
plt.show()

separate()
sns.boxplot(x="alive", y="age", hue="adult_male", data=titanic)
plt.show()


# Bokeh

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]

separate()
p = figure(title="Time-temperature relation", x_axis_label='Time', y_axis_label='Temperature')
p.line(x, y, legend_label="Temperature", line_width=4)
output_file("temperature.html")
show(p)

plot_1 = figure(plot_width=300, tools='pan,box_zoom')
plot_2 = figure(plot_width=300, plot_height=300, x_range=(0, 8), y_range=(0, 8))
plot_3 = figure()

separate()
plot_1.legend.orientation = "horizontal"

separate()
plot_1.legend.border_line_color = "red"

separate()
plot_1.legend.background_fill_color = "yellow"

separate()
plot_1.circle(np.array([1, 2, 3]), np.array([3, 2, 1]), fill_color='cyan')
show(plot_1)

separate()
plot_1.line([1, 2, 3, 4, 1], [5, 6, 7, 8, 9], line_width=4)
show(plot_1)

separate()
plot_2.multi_line(
    pd.DataFrame([[3, 2, 1], [9, 8, 7]]),
    pd.DataFrame([[1, 2, 3], [7, 8, 9]]),
    color="cyan"
)
show(plot_2)

separate()
save(plot_1)