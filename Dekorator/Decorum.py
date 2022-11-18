import time
import random

#dekorator

class dekoracja:

    #lista, w której przechowywane są czasy wykonania instancji funckji
    t_list= [] 

    # zmienne robocze do statystyki
    t_max= 0 # najdłuższy czas wykonania funkcji
    t_min=0  # najkrótszy czas wykonania funkcji
    t_avg=0  # średni czas wykonywania funkcji
    t_exc=0  # czas pojedyńczego wykonania funckji

    def __init__(self, func) :
        self.func = func
        
    def __call__(self):

        t1 = time.time() #zliczenie czasu przed wykonaniem dekorowanej funkcji
        self.func()   #uruchomienie dekorowanej funkcji  
        t2 = time.time() #zliczenie czasu po wykonaniu dekorowanej funkcji


        # Dodanie do listy i aktualizacja statystyki
        dekoracja.t_exc= t2-t1
        dekoracja.t_list.append(dekoracja.t_exc)
        dekoracja.t_list.sort()
        dekoracja.t_min = min(dekoracja.t_list)
        dekoracja.t_max = max(dekoracja.t_list)
        dekoracja.t_avg= sum(dekoracja.t_list) / len(dekoracja.t_list)


        print()
        print('Statystyka czasu')
        print('Czas realizacji tej instancji funkcji :', dekoracja.t_exc)
        print('Średni szas realizacji tej funkcji:', dekoracja.t_avg )
        print('Minimalny czas realizacji tej funkcji:', dekoracja.t_min)
        print('Maksymalny czas realizacji tej funkcji:', dekoracja.t_max)


# Testowana funkcja

@dekoracja
def spanko():
    from time import sleep
    sleep(random.randint(1,8)) #random uzyty w celu uzyskania różnych czasów


# test działania dekoratora

spanko()

spanko()

spanko()

