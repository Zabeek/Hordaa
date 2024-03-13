import random
import numpy as np


def aktualizacja_parametrow(a, b, wygrana):
    a_nowe = a + 0.5 * wygrana * (wygrana - a) / (b ** 2 + 1)
    b_nowe = b + 0.5 * (wygrana - a) * (wygrana - a) / (b ** 2 + 1)
    return a_nowe, b_nowe


def oblicz_wygrana_hordy(wygrane):
    wygrana_hordy = np.sum(wygrane, axis=1)
    return np.max(wygrana_hordy)


def symulacja_kasyna(N, M, f_prawdziwy, Tmax):
    # Inicjalizacja parametrów a_ij i b_ij dla każdego gościa i maszyny
    a = np.ones((M, N))
    b = np.ones((M, N))
    # Inicjalizacja listy przechowującej wygrane
    wygrane = np.zeros((M, N))

    # Pętla symulująca gry dla każdego kroku czasowego
    for t in range(Tmax):
        # Symulacja gry dla jednorękich bandytów
        for i in range(N):
            for j in range(M):
                # Generowanie wygranej zgodnie z rozkładem f_prawdziwy[i]
                wygrana = np.random.normal(f_prawdziwy[i], 1)
                # Aktualizacja parametrów a_ij i b_ij dla każdego gościa i maszyny
                a[j][i], b[j][i] = aktualizacja_parametrow(a[j][i], b[j][i], wygrana)
                # Dodanie wygranej do listy wygranych
                wygrane[j][i] = wygrana

        # Wyświetlanie wyników co pewną liczbę kroków czasowych
        if t % 1000 == 0:
            print(f"Krok czasowy: {t}")
            for j in range(M):
                print(f"Wyniki dla gościa {j + 1}:")
                print(wygrane[j])
                print()

            # Obliczenie i wyświetlenie maksymalnej wygranej hordy
            max_wygrana_hordy = oblicz_wygrana_hordy(wygrane)
            print(f"Maksymalna wygrana hordy: {max_wygrana_hordy}\n")

    return wygrane


# Parametry symulacji
N = 100  # liczba jednorękich bandytów
M = 50  # liczba gości
Tmax = 10000  # liczba kroków czasowych
f_prawdziwy = [random.uniform(0, 1) for _ in range(N)]  # rozkład prawdopodobieństwa wygranej dla każdego bandyty

# Wywołanie funkcji symulującej kasyno
wyniki_symulacji = symulacja_kasyna(N, M, f_prawdziwy, Tmax)
