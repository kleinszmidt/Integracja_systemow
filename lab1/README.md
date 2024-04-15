# Laboratorium 1- PYTHON
Wykonane zostało 10 zadań w języku **Python**. 

#### Przykładowe rozwiązanie poszczególnych zadań:

### Kod do zadania 5:
    import math 


    def find_square_root(value):
        return math.sqrt(value)


    if __name__ == '__main__':
        square_roots = []

    for i in range(1, 257):
        if find_square_root(i) % 2 == 0:
            square_roots.append(i)

    if square_roots:
        print(f"Liczby, których pierwiastek dzieli się przez 2 bez reszty: {square_roots}")
    else:

        print("Nic nie znaleziono")

### Wynik działania programu to:
Liczby, których pierwiastek dzieli się przez 2 bez reszty: 
#### [4, 16, 36, 64, 100, 144, 196, 256]

