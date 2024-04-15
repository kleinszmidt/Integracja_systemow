import random
import string


def generate_pseudo_string(length_of_string):
    return ''.join(random.choices(string.ascii_letters, k=length_of_string))


zmienna_24013 = dict()

if __name__ == '__main__':
    for i in range(10, 21):
        zmienna_24013[i] = ''.join(random.choices(string.ascii_letters, k=8))

    for key, value in zmienna_24013.items():
        print(f"{key} - {value}")

    print(f"Moj słownik to: {zmienna_24013}")