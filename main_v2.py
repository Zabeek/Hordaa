import numpy as np


def aktualizacja_parametrow(a, b, wygrana):
    a_nowe = a + 0.5 * wygrana * (wygrana - a) / (b ** 2 + 1)
    b_nowe = b + 0.5 * (wygrana - a) * (wygrana - a) / (b ** 2 + 1)
    return a_nowe, b_nowe


def oblicz_wygrana_hordy(wygrane):
    wygrana_hordy = np.sum(wygrane, axis=1)
    return np.max(wygrana_hordy)


def symulacja_kasyna(N, M, f_prawdziwy, Tmax, krok_wyswietlania=1000):
    a = np.ones((M, N))
    b = np.ones((M, N))
    wygrane = np.zeros((M, N))

    for t in range(Tmax):
        wygrane_losowe = np.random.normal(f_prawdziwy, 1, size=(M, N))
        wygrane += wygrane_losowe

        a, b = aktualizacja_parametrow(a, b, wygrane_losowe)

        if t % krok_wyswietlania == 0:
            print(f"Krok czasowy: {t}")
            max_wygrana_hordy = oblicz_wygrana_hordy(wygrane)
            print(f"Maksymalna wygrana hordy: {max_wygrana_hordy}\n")

    return wygrane


N = 100  # liczba jednorękich bandytów
M = 50  # liczba gości
Tmax = 10000  # liczba kroków czasowych
f_prawdziwy = np.random.uniform(0, 1, size=N)  # rozkład prawdopodobieństwa wygranej dla każdego bandyty

wyniki_symulacji = symulacja_kasyna(N, M, f_prawdziwy, Tmax)
