def main():
    inpt = input("Input: ").strip()
    print(shorten(inpt))


def shorten(str_inpt):
    lower_list = ['a', 'e', 'i', 'o', 'u']
    upper_list = ['A', 'E', 'I', 'O', 'U']

    for letter in str_inpt:
        if letter in lower_list or letter in upper_list:
            str_inpt = str_inpt.replace(letter, '')

    shorten_str = f"output: {str_inpt}"
    return shorten_str


if __name__ == "__main__":
    main()
