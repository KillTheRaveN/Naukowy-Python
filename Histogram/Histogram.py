
# Importy
from ascii_graph import Pyasciigraph
from ascii_graph.colors import *
from ascii_graph.colordata import vcolor
from rich.progress import track
import time

# Poczatkowe elementy
Nazwa = 'cierpienia-mlodego-wertera.txt'
Ilosc_max = 10
Dlugosc_min= 4
hist = {}

for i in track(range(20)):
    time.sleep(0.05)

# Otworzenie pliku z polskimi znakami
with open (Nazwa,  'r', encoding='UTF-8') as f:
    
    # usuniecie znakow specjalnych i rozdzielenie tekstu na pojedyncze slowa
    for line in f:
        temp = line.strip().replace('.','').replace(',','').replace('?','').replace('!','').replace('...','').lower().split(' ')
    
        # filtr dlugosci wyrazów
        temp = list(filter(lambda x : len(x) >= Dlugosc_min , temp))

        # liczenie słów
        for word in temp:
            if word not in hist:
                hist[word] = 0
            hist[word] += 1

    #sortowanie i ograniczenie ilości wyświetlanych elementów    
    sortownica = []
    for key in hist:
        sortownica.append((key, hist[key]))
    sortownica.sort(key=lambda x: x[1])
    sortownica = sortownica[::-1]
    sortownica = sortownica[:Ilosc_max]

    # Wizualizacja
    Graph= Pyasciigraph()
    pattern = [Blu, Yel, Gre]
    data = vcolor(sortownica, pattern)
    for line in Graph.graph('Najbardziej cierpiące wyrazy', data):
        print(line)