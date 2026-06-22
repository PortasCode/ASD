"""
Mateusz Portka


Niestety ja chyba nie mam nic, nie wiem zbytnio jak przechowywac tę kwota ktora teraz mamy w portfelu oraz mam problem z pomijaniem transakcji ktore na siebie nachodza
Chyba, że jako szczerosc potraktujemy jako poprawność działania algorytmu, to chętnie przygarnę ten 1 pkt, bo brakuje mi tylko 0.3 pkt do zdania
"""

from kol3_test import runtests


def transactions(M, T):
    n = len(T)
    najwiekszy_czas_zakoczenia = max(x[1] for x in T)

    zakoncznia_transakcji = [[] for _ in range(najwiekszy_czas_zakoczenia + 1)]
    for krotka in T:
        zakoncznia_transakcji[krotka[1]].append(krotka)

    dp = [0 for _ in range(najwiekszy_czas_zakoczenia + 1)]

    dp[0] = M

    for i in range(1, najwiekszy_czas_zakoczenia + 1):
        dp[i] = dp[i - 1]

        for transakcja in zakoncznia_transakcji[i]:
            portfel_wtedy = dp[transakcja[0] - 1]
            if portfel_wtedy >= transakcja[2]:
                portfel_po_transakcji = portfel_wtedy - transakcja[2] + transakcja[3]
                dp[i] = max(dp[i], portfel_po_transakcji)

    return dp[najwiekszy_czas_zakoczenia]


runtests(transactions, all_tests=True)
