# Readme

**_open()_** - funkcja służąca do otwierania plików (domyślnie w trybie 'readonly'). Otwarcie pliku w trybie 'rb' pozwala nam odczytywać bajty pliku. Tryb 'a' pozwala nam na dołączanie do pliku kolejnych znaków (bez nadpisywania zawartości pliku).

**_file.close()_** - funkcja służąca do zamykania otwartego wcześniej pliku. Należy pamiętać o jej wywołaniu, w przeciwnym wypadku możemy doprowadzić do wycieku pamięci Możemy także skorzystać z instrukcji _with_.

**_read()_** - odczytuje całą zawartość pliku (lub odpowiednią ilość bajtów).

**_readline()_** - odczytuję całą linię tekstu (lub odpowiednią ilość bajtu z niej)

**_readlines()_** - odczytuje wczystkie linie tekstu i zwraca je jako listę stringów (możemy po niej iterować).

**_write()_** - zapisuje do pliku przekazany ciąg znaków.

**_\_\_file\_\__** - specjalny atrybut zwracający ścieżkę do pliku ze skryptem.

## dos2unix.py

Skrypt ten pozwala na konwersję plików zawierająch znaki \r\n na końcu linii (Windows) na \n (Unix).

## Własna klasa do zarządzania plikami

Możemy stworzyć własną klasę do zarządzania plikami, która sama będzie zajmowała się otwieranie i zamykaniem pliku w odpowiednim momencie. Użyć do tego można atrybutów:
- **_\_\_enter\_\__** - ta metoda jest wywoływana podczas wchodzenia do bloku __with__
- **_\_\_exit\_\__** - ta metoda jest wywoływana podczas wychodzenia z bloku __with__

## PngReader

Klasa służąca do odczytywania plików PNG, lecz z pominięciem ich nagłówków. Dzięki temu możemy odczytać bezpośrednio zawartośc danego pliku.