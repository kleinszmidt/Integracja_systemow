from utils.obliczenia import my_abs, my_pow, silnia, iloczyn_skalarny

a = -5.4
b = 3
c = 5
lista = [1, 2, 3, 4]
if __name__ == '__main__':
    print(f"Wartość bezwzględna liczby {a} to {my_abs(a)}.")
    print(f"Liczba {b} podniesiona do potęgi {c} to {my_pow(b, c)}.")
    print(f"Silnia liczby {c}  to {silnia(c)}.")
    print(f"Iloczyn sklarany liczb z listy {lista} to {iloczyn_skalarny(lista)}.")
    print(abs(-4.5))