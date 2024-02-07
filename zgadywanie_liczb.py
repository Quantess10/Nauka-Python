import random

def wybrany_poziom(a, b):
    losowa_liczba = random.randint(a, b)  
    print("Zgadnij liczbę od ", a, " do ", b)
    while True:
        while True:
            dane_wejsciowe = input("Podaj liczbę: ")
            try:
                liczba = int(dane_wejsciowe)
                break
            except ValueError:
                print("Nie oszukuj! Podaj liczbę!")  

        if liczba > b:
            print("Podaj liczbę z zakresu ", a, "-", b, "!")

        elif liczba < a:
            print("Podaj liczbę z zakresu ", a, "-", b, "!")

        else:
            if liczba == losowa_liczba:
                print("Brawo! Udało Ci się odgadnąć liczbę! :) :) :)")
                break

            else:
                print("Próbuj dalej :)")
                if liczba < losowa_liczba:
                    print("Wskazówka: Liczba do odgadnięcia jest większa.")

                else:
                    print("Wskazówka: Liczba do odgadnięcia jest mniejsza.")                          

while True:
    print("Gra w zgadywanie liczb.")
    print("Wybierz poziom trudności:")
    print("1 - Łatwy (liczby z zakresu 1-10)")
    print("2 - Średni (liczby z zakresu 1-50)")
    print("3 - Trudny (liczby z zakresu 1-100)")
    print("0 - Zakończ grę.")
    dane_wejsciowe = input("Wybieram poziom: ")
    try:
        poziom = int(dane_wejsciowe)
        if poziom == 1:
            wybrany_poziom(1, 10)
        elif poziom == 2:
            wybrany_poziom(1, 50)
        elif poziom == 3:
            wybrany_poziom(1, 100)
        elif poziom == 0:
            print("Dzięki za grę w zgadnij liczbę :)")
            break   
        else:
            print("Podaj właściwą liczbę dla poziomu trudności!")
    except ValueError:
        print("Podaj właściwą liczbę dla poziomu trudności!")