class DrzewoPunktPrzedzial:
    def __init__(self, tablica):
        self.N = len(tablica)
        self.tree = [0] * (4 * self.N)
        self.build_tree(tablica, 0, 0, self.N - 1)

    def build_tree(self, tablica, indeks, lewy, prawy):
        if lewy == prawy:
            self.tree[indeks] = tablica[lewy]
            return

        srodek = (lewy + prawy) // 2

        self.build_tree(tablica, indeks * 2 + 1, lewy, srodek)
        self.build_tree(tablica, indeks * 2 + 2, srodek + 1, prawy)
        self.tree[indeks] = self.tree[2 * indeks + 1] + self.tree[2 * indeks + 2]

    def update_point(self, wezel, wartosc, indeks=0, lewy=0, prawy=None):
        if prawy is None:
            prawy = self.N - 1
        if lewy == prawy:
            self.tree[indeks] = wartosc
            return

        srodek = (lewy + prawy) // 2

        if wezel <= srodek:
            self.update_point(wezel, wartosc, indeks * 2 + 1, lewy, srodek)
        else:
            self.update_point(wezel, wartosc, indeks * 2 + 2, srodek + 1, prawy)

        self.tree[indeks] = self.tree[indeks * 2 + 1] + self.tree[indeks * 2 + 2]

    def query(self, q_left, q_right, indeks=0, left=0, right=None):
        if right is None:
            right = self.N - 1

        if q_right < left or q_left > right:
            return 0

        if left >= q_left and q_right <= right:
            return self.tree[indeks]

        srodek = (left + right) // 2
        return self.query(q_left, q_right, 2 * indeks + 1, left, srodek) + self.query(
            q_left, q_right, 2 * indeks + 2, srodek + 1, right
        )
