def bubble_sort(tablica):
    """
   Cel: Opanować prosty algorytm sortowania przez porównywanie sąsiadów. Narysuj diagram blokowy, potem zaimplementuj.
​

Diagram blokowy (tekstowy opis):

Start → Inicjuj i=0, n=długość tablicy.

Pętla zewnętrzna: i < n-1? → Tak: Pętla wewnętrzna j=0 do n-i-2.

Jeśli tab[j] > tab[j+1]: Zamień → j++ → Koniec wewnętrznej?

Nie: i++ → Koniec.
​

Implementacja Python:

text
def bubble_sort(arr):     n = len(arr)     for i in range(n):         for j in range(n - i - 1):             if arr[j] > arr[j + 1]:                 arr[j], arr[j + 1] = arr[j + 1], arr[j]     return arr
Test: [64, 34, 25, 12, 22, 11, 90] → [11, 12, 22, 25, 34, 64, 90].
    """

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
