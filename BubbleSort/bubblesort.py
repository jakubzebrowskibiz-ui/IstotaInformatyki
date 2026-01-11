def bubble_sort(tablica):
    """
  Cel: Opanować prosty algorytm sortowania przez porównywanie sąsiadów. Narysuj diagram blokowy, potem zaimplementuj.
​

Diagram blokowy (tekstowy opis):

Start → Inicjuj i=0, n=długość tablicy.

Pętla zewnętrzna: i < n-1? → Tak: Pętla wewnętrzna j=0 do n-i-2.

Jeśli tab[j] > tab[j+1]: Zamień → j++ → Koniec wewnętrznej?

Nie: i++ → Koniec.
    """

    # Diagram blokowy (opis tekstowy):
    # START
    # Inicjalizuj i = 0
    # n = długość tablicy
    #
    # Czy i < n - 1?
    # ├── NIE → STOP
    # └── TAK
    #      Inicjalizuj j = 0
    #      Czy j < n - i - 1?
    #      ├── NIE → i = i + 1 → powrót do sprawdzenia i
    #      └── TAK
    #           Czy tab[j] > tab[j + 1]?
    #           ├── TAK → Zamień tab[j] i tab[j + 1]
    #           └── NIE → bez zmiany
    #           j = j + 1 → powrót do sprawdzenia j

    n = len(tablica)

    # Pętla zewnętrzna
    for i in range(n):
        # Pętla wewnętrzna
        for j in range(0, n - i - 1):
            # Porównanie sąsiadów
            if tablica[j] > tablica[j + 1]:
                # Zamiana miejscami
                tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]

    return tablica


# Test algorytmu
dane = [64, 34, 25, 12, 22, 11, 90]
wynik = bubble_sort(dane)

print("Posortowana tablica:", wynik)
