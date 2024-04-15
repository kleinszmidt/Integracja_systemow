def chech_character(our_input):
    if our_input.isdigit():
        return True
    else:
        return False


if __name__ == '__main__':
    input_wej = input("Podaj znak lub znaki: ")

    if len(input_wej) > 0:
        if chech_character(input_wej[0]):
            print(f"Podany znak jest cyfrą")
        else:
            print(f"Podany znak nie jest cyfrą")
    else:
        print(f"Nie wpisałeś żadnego znaku")