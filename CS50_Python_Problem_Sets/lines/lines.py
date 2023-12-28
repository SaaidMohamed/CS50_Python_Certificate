from sys import argv, exit


def main():
    check_argv()

    with open(argv[1], "r") as file:
        lines = file.readlines()
    count = 0
    for line in lines:
        if check_emptylines_coments(line):
            count = count
        else:
            count = count + 1

    print(count, end="")


def check_argv():
    if len(argv) == 1:
        exit("Too few command_line arguments")
    if len(argv) > 2:
        exit("Too many command_line arguments")
    try:
        if argv[1].endswith(".py") == False:
            exit("Not a python file")
    except FileNotFoundError:
        exit("File does not exist")  #


def check_emptylines_coments(line):
    if line.isspace():
        return True
    line = line.strip()
    if line.startswith("#"):
        return True


main()
