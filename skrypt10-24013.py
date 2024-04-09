def ascii_to_letters(number):
    return chr(number)

if __name__ == '__main__':
    letters = []
    for i in range(65, 91):
        letters.append(ascii_to_letters(i))
    letters_string = (''.join(letters))

    with open("alfabet1-24013.txt", "w") as file:
        file.write(letters_string)

    with open("alfabet2-24013.txt", "w") as file:
        for literka in letters_string:
            file.write(f"{literka}\n")

