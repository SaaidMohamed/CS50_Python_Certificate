def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if two_char(s) and check_str_ends_with_digit(s) and str_length(s) and check_punctuation(s) and check_str_digit_starts_with_0(s) :
        return True
    else:
        return False


def two_char(st):
    if st and st[0:2].isalpha():
        return True
    else:
        return False


def check_str_ends_with_digit(st):
    boal = True
    if st[2:len(st)-1].isalpha() and st[-1].isalpha() == False :
        boal = False
    if st[2:len(st)-1].isdigit() and st[-1].isdigit() == False or  st[2:len(st)-2].isdigit() and st[-1].isdigit() or  st[2:len(st)-3].isdigit() and st[-1].isdigit():
        boal = False
    else :
        boal = True

    return boal


def str_length(st):
    if len(st) > 6 or len(st) <2 :
        return False
    else:
        return True


def check_punctuation(st):
    punct_list = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', ' ', '-',
                 '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', "\ ", ']', '^', '_', '`', '{', '|', '}', '~']

    for punct in punct_list:
        boal = True
        if punct in st:
            boal = False
            break
        else:
            boal = True
    return boal


def check_str_digit_starts_with_0(st):
    counter = 0
    for i in st:
        boal = True
        if ord(i)>=48 and ord(i)<=57 and counter == 0:
            counter = counter + 1
            if ord(i) == 48 and counter == 1:
                counter = counter + 1
                boal = False
                break
        else:
            boal = True
    return boal

if __name__ == "__main__":
    main()

