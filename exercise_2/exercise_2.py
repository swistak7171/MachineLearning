import pandas as pd
import matplotlib.pyplot as plt
import datetime

data = pd.read_csv(filepath_or_buffer='samochody1tys.csv', verbose=True)


def separate(number):
    print(f'=========== {number} ===========')


def full_print(frame):
    with pd.option_context('display.max_rows', None, "display.max_columns", None):
        print(frame)


# Tworzy obiekt DataFrame i wyświetla tabelę z wczytanymi danymi
separate(1)
frame = pd.DataFrame(data)
print(frame)

# Wyświetla tabelę z samochodami marki Nissan, które zostały wyprodukowane przez 2015 rokiem
separate(2)
full_print(frame.query(
    'marka == "Nissan" and rok_produkcji < 2015'
))

# Zmienia nazwę kolumn na bardziej przystępne
separate(3)
full_print(frame.rename(columns={
    'id': 'ID',
    'marka': 'Marka',
    'model': 'Model',
    'rok_produkcji': 'Rok produkcji',
    'rodzaj_silnika': 'Rodzaj silnika',
    'pojemnosc_silnika': 'Pojemność silnika',
    'przebieg': 'Przebieg',
    'cena': 'Cena',
    'wojewodztwo': 'Województwo'
}))

# Sortuje samochody od najdroższych do najtańszych
separate(4)
print(frame.sort_values('cena', ascending=False))

# Wyświetla tylko markę, model i cenę samochodów
separate(5)
print(frame[['marka', 'model', 'cena']])

# Wyświetla statystyki danych (liczbę rekordów, ich unikalność, średnią itp.)
separate(6)
full_print(frame.describe(include='all'))

# Wyświetla liczbę wierszy, medianę każdej kolumny, sumę wartości,
# wartość najmniejszą i największą w każdej kolumnie
separate(7)
print('COUNT')
print(frame.count())
print('MEDIAN')
print(frame.median())
print('SUM')
print(frame.sum())
print('MIN')
print(frame.min())
print('MAX')
print(frame.max())

# Dodaje kolumnę z liczbą lat samochodu
separate(8)
yearsFrame = frame.copy()
currentYear = datetime.datetime.now().year
yearsFrame['lata'] = currentYear - yearsFrame['rok_produkcji']
print(yearsFrame[['id', 'marka', 'model', 'rok_produkcji', 'lata']])

# Wyświetla wykres obrazujący zależność ceny od roku produkcji
separate(9)
frame.plot.scatter(x='rok_produkcji', y='cena')
plt.show()

# Usuwa kolumnę pojemnosc_silnika, rodzaj_silnika, cena oraz wojewodztwo
separate(10)
print(frame.drop(columns=['pojemnosc_silnika', 'rodzaj_silnika', 'cena', 'wojewodztwo']))

# Wybiera 3 pierwsze samochody, które mają przebieg większy niż 250000
separate(11)
print(frame[frame['przebieg'] > 250000].head(3))
