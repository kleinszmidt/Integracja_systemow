import random
import string
from collections import Counter

def occurences(text):
    acc = []
    my_dict = Counter(text)
    for key, value in my_dict.items():
        acc.append((key, value))
    return acc

if __name__ == '__main__':
    text_value = ''.join(random.choices(string.ascii_letters, k=100))
    wynik = occurences(text_value)
    print (f"Liczba unikalnych znaków to {len(wynik)}")
    for index, liczba_wystapien in enumerate(wynik):
        print(f"{index}: {liczba_wystapien}")