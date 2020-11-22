# Readme

Na początku ładujemy pobrany model za pomocą funkcji _load()_.

## 1
Przekazany tekst jest zamieniamy na obiekt typu _Doc_, w którym jest nasz string podzielony na odpowiednie częście.

## 2
To samo możemy zrobić wczytując tekst z pliku za pomocą funkcji _open()_ i _read()_.

## 3
Istnieje także możliwość podzielenia tekstu za zdania. Aby się mieć do nich dostęp należy odwołać się do pola _sents_ w obiekcie _Doc_. Tekst jest dzielony na zdania według znaku kroki.

## 4
Możemy także dzielić tekst na zdania według innych znaków, nie tylko kropki. Aby to zrobić musimy dodać nową "regułę", używając metody _add_pipe()_.

## 5
Tokeny, czyli części, na jakie został podzielony nasz tekst, posiadają różne atrybuty, takie jak np.:
- _text_with_ws - zwraca tekst z następującą po nim spacją (jeśli takowa się tam znajduje)
- _is_alpha_ - zwraca True, jeśli tekst składa ze znaków alfabetu
- _is_space_ - zwraca True, jeśli token jest spacją

## 6
Możemy zdefiniować własne zasady dzielenia tekstu na tokeny. Używamy to tego klasy _Tokenizer_, do którego przekazujemy odpowiednie obiekty używające Regexu. W tym przypadku chcemy podzielić na tokeny także słowa połączone myślnikiem. Tworzymy Regex i przekazujemy go do _Tokenizera_.

## 7
Token posiada atrybut _is_stop_, który określa czy dany token jest tzw. "stop word", czyli słowem o małym znaczeniu (spójnikiem), niewpływającym na identyfikację dokumentu. Taki słowem jest np. "i" oraz "oraz".

## 8
Lematyzacja to proces, który pomaga w normalizacji tekstu. "Wychwytywane" są wszystkie słowa, które pochodzą od jednego słowa, lecz są np. w różnych odmianach czy liczbach. Dzięki temu takie słowa jak "zadania", "zadaniem", "zadań" są traktowane jako jeden token ("zadanie").

## 9
Możemy także liczyć wystąpienia danych słów w tekście. Służy do tego klasa _Counter_. Możemy dzięki niej wyszukaj najpopularniejsze słowa czy te, które wystąpiły np. tylko raz.

## 10
POS tag to specjalne oznaczenie tokenu odnośnie części mowy. Przykładowo słowo "ma" zostanie oznaczone jako czasownik, a "kot" jak rzeczownik. Funkcja _spacy.explain()_ zwraca szczegóły tagu.

## 11
Można wykonać wizualizację tekstu za pomocą modułu _displaCy_. Funkcja _serve()_ tworzy graf zależności, można go obejrzeć pod adresem "http://127.0.0.1:5000", gdyż uruchamiany jest wtedy serwer HTTP z wykresem.

## 12
Aby przekształcić tekst pierwotny do tekstu, który można analizować, należy stworzyć funkcję, która:
- przekształci tekstu do postaci małych liter
- wyhasłuje każdy token
- usunie znaki interpunktcyjne i "stop words"
Tekst, zwrócony przez tę funkcję, powinien być gotowy do analizy.

## 13
_Rule-based matching_ to proces "wyłuskiwania" informacji z nieuporządkowanego tekstu. Tworzymy wzór, który posłuży nam do identyfikacji i wyciągania pasujących tokenów. Możemy przykładowo stworzyć wzór, który będzie symbolizował numer telefonu.

## 14
Parsowanie zależności do proces wydobywania struktury gramatycznej tekstu. Pozwala zdefiniować zależności między hasłami a ich zależności. Główny człon zdania nie ma zależności i jest nazywany rdzeniem zdania. Atrybuty tokenów _head_ i _dep__ pozwalają zobaczyć te zależności.

## 15
Istnieje możliwość nawigacji do drzewie zależności, za pomocą takich funkcji i właściwości jak np.
- _children_ (potomkowie tokenu)
- _nbor_ (sąsiadujący węzeł)
- _lefts_ (tokeny po lewej)
- _rights_ (tokeny po prawej)

## 16
Porcjonowanie to proces podziału nieuporządkowanego tekstu na frazy. Dzięki temu analiza tekstu jest o wiele prostsza, gdyż kilka tokenów może być połączonych w logiczną znaczeniowo frazę. Przykładowo, do podziału tekstu na frazy nominalne służy funkcja _noun_chunks()_.

## 17
Fraza werbalną jest frazą, która składa się z przynajmniej jednego czasownika. Aby podzielić też na frazy werbalne należy pobrać bibliotekę _textacy_, stworzyć wzór i użyć funkcji _pos_regex_matches()_, która porówna tekst do wzoru i podzieli tekst na żądane frazy.

## 18
_NER_ to proces znajdowania podobnych znaczeniowo nazwanych encji w nieuporządkowanych tekście i klasyfikowania ich według predefiniowanych kategorii. Przykładowo, możemy sklasyfikować kilka rzeczowników jako nazwy miast. NER pozwala nam dowiedzieć się więcej na temat znaczenia tekstu. Aby wykorzystać NER należy odwołać się do właściwości _ents_, która zwraca encje dokumentu. Możemy użyć wykresu _ent_ z modułu _displaCy_, by zobrazować podział tekstu po użyciu NER. Tego procesu możemy używać także np. do wykrywania i zamieniania różnych fraz, np. usuwania wulgaryzmów.