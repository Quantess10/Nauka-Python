print("Kalkulator v.1.0 - działania na dwóch liczbach.")

def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def pomnoz(a, b):
    return a * b

def podziel(a, b):
    if b == 0:
        return "Nie dziel przez zero ty cholero!"
    return a / b

dozwolone_znaki = {'+', '-', '*', '/'}
kontynuuj = 't'

while kontynuuj == 't':
    while True:
        dane_wejsciowe = input("Podaj pierwszą liczbę: ")
        try:
            liczba1 = float(dane_wejsciowe)
            break
        except ValueError:
            print("Nie oszukuj! To nie jest liczba!")

    while True:
        dane_wejsciowe = input("Podaj drugą liczbę: ")
        try:
            liczba2 = float(dane_wejsciowe)
            break
        except ValueError:
            print("Nie oszukuj! To nie jest liczba!")        

    while True:
        znak = input("Podaj znak działania (+, -, *, /): ")
        if znak in dozwolone_znaki:
            break
        else:
            print("Niedozwolony znak. Spróbuj ponownie.")

    if znak == '+':
        wynik = dodaj(liczba1, liczba2)

    elif znak == '-':
        wynik = odejmij(liczba1, liczba2)

    elif znak == '*':
        wynik = pomnoz(liczba1, liczba2)

    elif znak == '/':
        wynik = podziel(liczba1, liczba2)        

    print(liczba1, znak, liczba2, '=', wynik)    
    kontynuuj = input("Czy chcesz kontynuować (t/n)? ")