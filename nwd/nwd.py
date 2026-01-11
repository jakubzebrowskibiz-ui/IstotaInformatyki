def nwd(a, b):
    """
NWD Algorytmem Euklidesa
Cel: Zrozumieć rekurencyjną naturę algorytmu Euklidesa do obliczania największego wspólnego dzielnika (NWD). Praca w parach: jedna osoba pisze pseudokod, druga testuje w Pythonie.
​

Kroki:

Zapisz pseudokod: FUNKCJA NWD(a, b): DOPÓKI b ≠ 0: zamień [a, b] na [b, a MOD b]; KOŃCÓWKA: zwróć a.
​

Zaimplementuj w Pythonie (lub dowolnym wybranym języku) iteracyjnie:

text
def nwd(a, b):     while b != 0:         a, b = b, a % b     return a
    """

    while b != 0:
        a, b = b, a % b

    return a


# Przykładowe testy
liczba1 = 48
liczba2 = 18

wynik = nwd(liczba1, liczba2)
print(f"NWD({liczba1}, {liczba2}) = {wynik}")
