
def find_index(input_string, string_to_find):
    return input_string.find(string_to_find)


if __name__ == '__main__':
    input_wej = input("Podaj tekst w którym będziesz szukać: ")
    what_to_find = input("Czego szukasz?: ")
    index = find_index(input_wej, what_to_find)
    print(f"Długość tekstu to {len(input_wej)}.")
    if index >= 0:
        print(f"Szukamy ciąg znaków zaczyna sie od indeksu {index}.")
    else:
        print("Nic nie znaleziono")