# Readme

## JSON

*_json.dump()_* - serializuje przekazany obiekt do formatu JSON i zapisuje bajty do drugiego przekazanego obiektu.

*_json.dumps()_* - serializuje przekazany obiekt i zwraca JSON w postaci stringa. Możemy przekazać także wartość wcięcia (_indent_).

*_json.load()_* - deserializuje przekazany odnośnik do pliku z obiektem JSON na odpowiedni obiekt Pythonowy.

*_json.loads()_* - deserializuje przekazany obiekt JSON w postaci stringa na odpowiedni obiekt Pythonowy. Możemy także przekazać zaimplementowany deserializator.

*_requests.get()_* - wysyła request HTTP typu GET pod wskazany adres.

*_sorted()_* - sortuje przekazaną listę według odpowiedniego warunku.

*_join()_* - tworzy z elementów listy string, gdzie elementy są rozdzielone przekazanym stringiem.

*_filtered()_* - filtruje przekazaną listę używając przekazanej referencji do metody filtrującej.

*_json.JSONEncoder_* - klasa, która pozwala nam samemu zaimplementować serializację danego typu.

*_isinstance()_* - sprawdza, czy przekazany obiekt jest danego typu.

## CSV

*_csv.reader()_* - zwraca obiekt czytający linię po linii (jako string) odpowiedni plik CSV (można przekazać jakim znakiem są rozdzielone dane).

*_csv.DictReader()_* - zwraca obiekt przekształcający linie pliku CSV w słownik.

*_csv.writer()_* - zwraca obiekt, który służy do zapisywania danych do pliku CSV. Może ustalić jakim znakiem będą rozdzielone dane czy jak wstawić do danych znak rozdzielający tak, by nie był on oznaczany jako znak rozdzielający.

*_csv.DictWriter()_* - zwraca obiekt, pozwalający zapisywać dane do pliku CSV ze słowników (możemy przekazać nazwy kolumn).

*_pandas.read_csv()_* - czyta plik CSV i przekształca go na obiekt typu DataFrame. Możemy ustalić, który kolumna jest indeksem oraz która kolumna jest np. datą i tak należy ją parsować. Można także przekazać nazwy kolumn.

*_DataFrame.to_csv()_* - zapisuje dany obiekt typu DataFrame do wskazanego pliku CSV.

