import sys
import heapq
from math import log

def main():
    dane = sys.stdin.read().split()

    if not dane:
        return

    n = int(dane[0])  # liczba schronisk
    m = int(dane[1])  # liczba ścieżek pomiędzy schroniskami
    k = int(dane[2])  # liczba najciekawszych schronisk

    G = [[] for _ in range(n + 1)]

    idx = 3
    for _ in range(m):
        u = int(dane[idx])
        v = int(dane[idx + 1])
        waga = int(dane[idx + 2])

        log_waga = log(waga)
        G[u].append((v, log_waga, waga))
        G[v].append((u, log_waga, waga))
        idx += 3

    najciekawsze = []
    for _ in range(k):
        najciekawsze.append(int(dane[idx]))
        idx += 1

    # parent[i] = (poprzedni_wierzcholek, prawdziwa_waga_krawedzi)
    parent = [(-1, -1) for _ in range(n + 1)]

    # dist[i] = [najlepszy czas logarytmiczny, liczba schronisk]
    dist = [[-1, -1] for _ in range(n + 1)]

    # Inicjalizacja wbudowanej kolejki priorytetowej
    Q = []
    # Wrzucamy krotkę: (czas, liczba_schronisk, wierzchołek)
    heapq.heappush(Q, (0.0, 1, 1))
    dist[1] = [0.0, 1]
    
    # Epsilon do bezpiecznego porównywania floatów
    EPS = 1e-9

    while Q:
        # Wyciągamy element o najmniejszym czasie (heapq automatycznie sortuje po pierwszym elemencie krotki)
        obecny_czas, obecne_schroniska, u = heapq.heappop(Q)

        # Sprawdzenie czy wyjęty stan nie jest już nieaktualny
        if obecny_czas > dist[u][0] + EPS or (abs(obecny_czas - dist[u][0]) < EPS and obecne_schroniska > dist[u][1]):
            continue

        for v, log_waga, prawdziwa_waga in G[u]:
            nowy_czas = obecny_czas + log_waga
            nowe_schroniska = obecne_schroniska + 1

            if (
                dist[v][0] == -1
                or nowy_czas < dist[v][0] - EPS
                or (abs(nowy_czas - dist[v][0]) < EPS and nowe_schroniska < dist[v][1])
            ):
                dist[v] = [nowy_czas, nowe_schroniska]
                parent[v] = (u, prawdziwa_waga)
                # Dodajemy nowy stan do kolejki
                heapq.heappush(Q, (nowy_czas, nowe_schroniska, v))

    # Odtwarzanie ścieżki i liczenie finalnego iloczynu
    for cel in najciekawsze:
        if dist[cel][0] == -1:
            continue
            
        sciezka = []
        obecny = cel
        calkowity_czas = 1
        
        while obecny != -1:
            sciezka.append(obecny)
            rodzic, waga_krawedzi = parent[obecny]
            
            if rodzic != -1:
                calkowity_czas *= waga_krawedzi
                
            obecny = rodzic
            
        sciezka.reverse()
        
        wynik = [str(len(sciezka))] + [str(x) for x in sciezka] + [str(calkowity_czas)]
        print(" ".join(wynik))


if __name__ == "__main__":
    sys.set_int_max_str_digits(50000) 
    main()

