# Zadanie nr 3

## Python Basics
_list.index(value)_ - zwraca indeks podanego elementu listy

_list.count(value)_ - liczy wystąpienia danego elementu listy

_list.sort()_ - sortuje listę od wartości najmniejszej do największej

_list.reverse()_ - odwraca kolejność elementów listy

_string.upper()_ - zwraca string z zamienionymi literami na wielkie litery


## NumPy Basics
_array.sum()_ - zwraca sumę wszystkich elementów tablicy

_array.min()_ - zwraca najmniejszą wartość z tablicy

_array.mean()_ - zwraca średnią wartość wszystkich elementów tablicy

_np.add(first, second)_ - dodaje do siebie dwie tablice

_np.sqrt(array)_ - oblicza pierwiastek z elementów tablicy

## SciPy - Linear Algebra

_np.asmatrix(values)_ - zamienia przekazane wartości na macierz

_matrix.I_ - zwraca macierz odwrotną

_matrix.T_ - zwraca macierz transponowaną

_linalg.det(matrix)_ - zwraca wyznacznik macierzy

_linalg.norm(matrix)_ - zwraca normę Frobeniusa macierzy

## Pandas Basics

_DataFrame.sort_values(by)_ - sortuje wartości na podstawie nazwy kolumny

_DataFrame.shape_ - zwraca wymiary obiektu

_DataFrame.sum()_ - sumuje wartości wierszy

_DataFrame.describe()_ - zwraca opis i własności obiektu

_DataFrame.apply(lambda)_ - stosuje przekazaną funkcję na wartościach obiektu

## Matplotlib

_plt.figure()_ - tworzy nową figurę (wykres)

_figure.add_subplot(rows)_ - dodaje osie do figury (wykresu)

_axes.plot(x, y)_ - zaznacza odpowiednie linie (wartości) na wykresie

_axes.scatter(x, y, marker)_ - zaznacza punkty na układzie współrzędnych

_plt.title(text)_ - nadaje tytuł wykresowi

_plt.savefig(filename)_ - zapisuje wykres do pliku graficznego

_plt.show()_ - wyświetla narysowany wykres w oknie

## Seaborn


_sns.countplot(x, data)_ - tworzy wykres słupkowy dla danych

_sns.barplot(x, y, hue, data)_ - tworzy wykres słupkowy dla danych

_sns.pointplot(x, y, hue, data)_ - tworzy wykres punktowy dla danych

_sns.violinplot(x, y, hue, data)_ - tworzy wykres skrzypcowy dla danych

_sns.boxplot(x, y, hue, data)_ - tworzy wykres pudełkowy dla danych

## Bokeh


_figure(title, x_label, y_label)_ - tworzy nowy wykres o tytule i etykietach

_figure.line(x, y)_ - tworzy wykres liniowy z danymi

_output_file(filename)_ - zapisuje utworzony wcześniej wykres do pliku o nazwie

_show(figure)_ - wyświetla wykres w przeglądarce

_figure.legend.orientation_ - pozwala ustawić orientację legendy wykresu

_figure.legend.border_line_color_ - pozwala ustawić kolor linii brzegowej legendy wykresu

_figure.legend_background_fill_color_ - pozwala ustawić kolor wypełnienia legendy wykresu

_figure.circle(x, y)_ - tworzy wykres kołowy

_save(figure)_ - zapisuje plik HTML z wykresem