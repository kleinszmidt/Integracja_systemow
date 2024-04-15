def find_all_indexes(input_string, string_to_find):
    acc = []
    for index1, value in enumerate(input_string):
        if value == string_to_find:
            acc.append(index1)
    return acc


if __name__ == '__main__':
    input_wej = input("Podaj tekst w którym będziesz szukać: ")
    what_to_find = input("Czego szukasz?: ")
    index = find_all_indexes(input_wej, what_to_find)
    print(f"Długość tekstu to {len(input_wej)}.")
    if index:
        print(f"Szukane indeksy to {index}")
    else:
        print("Nic nie znaleziono")