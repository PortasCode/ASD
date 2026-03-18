"""
=========================================
INSERTION SORT (Sortowanie przez wstawianie)
=========================================
Jak to działa?
Działa bardzo podobnie do układania kart w ręce. Bierzemy kolejny element
z części nieposortowanej i wstawiamy go w odpowiednie miejsce w części już
posortowanej, przesuwając większe od niego elementy w prawo.

Wizualizacja krok po kroku dla tablicy [5, 3, 6, 2]:
Start:  [5 | 3, 6, 2] (Pierwszy element z założenia stanowi "posortowaną" bazę)
Krok 1: Bierzemy 3. Porównujemy z 5. 5 jest większe, więc przesuwamy 5 w prawo i wstawiamy 3.
        [3, 5 | 6, 2]
Krok 2: Bierzemy 6. Porównujemy z 5. Jest większe, więc zostaje na swoim miejscu.
        [3, 5, 6 | 2]
Krok 3: Bierzemy 2. Porównujemy z 6, 5, 3, przesuwając je wszystkie kolejno w prawo.
        Wstawiamy 2 na sam początek.
        [2, 3, 5, 6 |]
Gotowe: [2, 3, 5, 6]

Złożoność obliczeniowa:
- Pesymistyczna: O(n^2) (Gdy tablica jest posortowana odwrotnie i każdy element trzeba
  przepchnąć na sam początek).
- Średnia: O(n^2)
- Optymistyczna: O(n) (Gdy tablica jest już posortowana, algorytm wykonuje tylko
  jedno porównanie dla każdego elementu i od razu idzie dalej).
"""

def insertion_sort(arr):
    n = len(arr)
    # Zaczynamy od drugiego elementu (indeks 1)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Przesuwamy elementy części posortowanej (0 do i-1),
        # które są większe od naszego 'key', o jedną pozycję w prawo
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Wstawiamy klucz w wyznaczone, puste miejsce
        arr[j + 1] = key

    return arr