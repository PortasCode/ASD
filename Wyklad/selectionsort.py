"""
=========================================
SELECTION SORT (Sortowanie przez wybieranie)
=========================================
Jak to działa?
Algorytm wirtualnie dzieli tablicę na dwie części: posortowaną (na początku)
i nieposortowaną (reszta). W każdej iteracji szuka najmniejszego elementu
w części nieposortowanej i zamienia go miejscami z pierwszym elementem
tej części nieposortowanej.

Wizualizacja krok po kroku dla tablicy [5, 3, 6, 2]:
Krok 1: [5, 3, 6, 2] -> Szukamy minimum z całości (to 2). Zamieniamy z pierwszym (5).
        [2 | 3, 6, 5]   (Znak '|' oddziela część posortowaną od nieposortowanej)
Krok 2: [2 | 3, 6, 5] -> Minimum z [3, 6, 5] to 3. Zamieniamy z pierwszym w nieposortowanej (3).
        [2, 3 | 6, 5]
Krok 3: [2, 3 | 6, 5] -> Minimum z [6, 5] to 5. Zamieniamy z (6).
        [2, 3, 5 | 6]
Gotowe: [2, 3, 5, 6]

Złożoność obliczeniowa:
- Pesymistyczna: O(n^2)
- Średnia: O(n^2)
- Optymistyczna: O(n^2) (Zawsze musi przeszukać resztę tablicy w poszukiwaniu minimum,
  nawet jeśli tablica jest już posortowana).
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Zakładamy, że najmniejszy element jest na obecnej pozycji 'i'
        min_idx = i

        # Szukamy mniejszego elementu w reszcie tablicy
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Jeśli znaleźliśmy mniejszy element, zamieniamy je miejscami
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr