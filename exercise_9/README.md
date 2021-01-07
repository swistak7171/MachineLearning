# Readme

### Oryginalny obraz
![](corgie.jpg)

### ROI
![](corgie_roi.jpg)

### Zmiana rozmiaru
![](corgie_resized.jpg)

### Obrócony
![](corgie_rotated.jpg)

### Obrócony i nie przycięty
![](corgie_bound_rotated.jpg)

### Rozmyty
![](corgie_blurred.jpg)

### Prostokąt
![](corgie_rectangle.jpg)

### Okrąg
![](corgie_circle.jpg)

### Linia
![](corgie_line.jpg)

### Tekst
![](corgie_text.jpg)

### Szary
![](corgie_gray.jpg)

### Krawędzie
![](corgie_edged.jpg)

### Threshold
![](corgie_thresh.jpg)

### Kontury
![](corgie_contours.jpg)

### Kontury z tekstem
![](corgie_contours_text.jpg)

### Redukcja pikseli
![](corgie_eroded.jpg)

### Rozszerzony
![](corgie_dilated.jpg)

### AND
![](corgie_bitwise.jpg)

## cv2
*_imread()_* - wczytuje obraz z pliku.

*_image.shape_* - pobiera właściwości kształtu obrazu (szerokość, wysokość, głębokość).

*_imshow()_* - wyświetla okno z obrazem.

*_waitKey()_* - czeka na wciśnięcie klawisza.

*_image[x, y]_* - pobiera wartości BGR danego piksela.

*_image[x1:x2, y1:y1]_* - pobiera wycinek obrazu o danych współrzędnych.

*_resize(image, (x, y))_* - zmienia wymiary obrazu na podane, ignorując proporcje obrazu.

*_getRotationMatrix(center, degree, scale)_* - tworzy macierz rotacji na podstawie środka obrazu, kąta obrotu i skali.

*_warpAffine(image, matrix, (width, height))_* - zwraca obrócony obraz na podstawie przekazanej macierzy obrotu.

*_GaussianBlur(image, kernel, sigma)_* - rozmywa obraz na podstawie przekazanych parametrów (im większy kernel tym bardziej rozmyty obraz).

*_rectangle(image, pt1, pt2, color, thickness)_* - rysuje na obrazie prostokąt, gdzie pt1 to lewy górny piksel, pt2 to prawy dolny piksel, color to wartość GBR koloru prostokąta i thickness to jego grubość w pikselach.

*_circle(image, center, radius, color, thickness)_* - rysuje na obrazie okrąg, gdzie center to piksel środkowy, radius to promień okręgu, color to wartość GBR koloru okręgu i thickness to jego grubość w pikselach (wartość ujemna zamalowuje cały okrąg na dany kolor).

*_line(image, pt1, pt2, color, thickness)_* - rysuje na obrazie linie, gdzie pt1 to piksel początkowy, pt2 to piksel końcowy, color to wartość GBR koloru linii i thickness to jej grubość w pikselach.

*_putText(image, text, start, font, scale, color, thickness)_* - rysuje na obrazie podany tekst, gdzie start to punkt początkoowy, font to wybrana przez nas czcionka, scale to skala tekstu, color to kolor tekstu, a thickness to jego grubość.

*_cvtColor(image, mode)_* - zmienia kolorystykę obrazu na podstawie przekazanego trybu (np. na szarość).

*_Canny(image, min, max)_* - znajduje krawędzie obiektów na obrazie używając algorytmu Canny, gdzie min to minimalny próg, a max - maksymalny.

*_threshold(image, thresh, max, type)_* - zmienia wartości pikseli na podstawie podanego progu i maksymalnej wartość używając przekazanego trybu.

*_findContours()_* - wykrywa krawędzie na obrazie (threshold).

*_drawContours()_* - rysuje wykryte kontury na obrazie.

*_erode()_* - redukuje szumy na obrazach i zmniejsza rozmiar obiektów na pierwszym planie.

*_dilate()_* - działa odwrotnie do erode().

*_bitwise_and()_* - używa maski to zmiany wartości pikseli na podstawie działania operacji AND na nich.

## imutils
*_resize(image, width, height)_* - zmienia wymiary obrazu, obliczając proporcje i dopasowując odpowiedni wymiar.

*_rotate(image, degree)_* - zwraca obrócony o daną ilość stopni obraz.

*_rotate_bound(image, degree)_* - zwraca obrócony o daną ilość stopni obraz, którego krawędzie nie są przycięte i są w całości widoczne.

*_grab_contours()_* - wykrywa kontury na obrazie.

## ArgumentParser
*_add_argument(name, fullname, required, help)_* - dodaje argument wejściowy do skryptu, gdzie name to jego skrócona nazwa, fullname to jego pełna nazwa, required określa czy jest wymagany, a help definiuje tekst, który jest wyświetlany w przypadku wpisania komendy --help.

