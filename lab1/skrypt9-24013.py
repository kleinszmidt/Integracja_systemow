class Vehicle:
    def __init__(self, nazwa, rok_produkcji, przebieg):
        self.nazwa = nazwa
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg

    def is_long_mileage(self):
        return self.przebieg > 100_000

    def is_old(self):
        return self.rok_produkcji < 2009

class Car:
    def __init__(self, nazwa, rok_produkcji, przebieg):
        self.nazwa = nazwa
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg

    def is_long_mileage(self):
        return self.przebieg > 100_000

    @property
    def is_old(self):
        return self.rok_produkcji < 2009

class Third(Car, Vehicle):
    pass

v1 = Vehicle("Ford", 1999, 200_000)
c1 = Car("Volvo", 2024, 2_000_000)
t1 = Third("Renault", 2003, 123_000)

print(v1.is_old(), v1.__class__)
print(c1.is_old)
print(t1.is_old)
