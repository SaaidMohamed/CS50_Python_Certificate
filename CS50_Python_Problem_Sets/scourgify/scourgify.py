from sys import argv, exit
import csv


def main():
    check_argv()
    read_write_file()


def check_argv():
    if len(argv) == 1 or len(argv) == 2:
        exit("Too few command_line arguments")
    if len(argv) > 3:
        exit("Too many command_line arguments")
    try:
        if argv[1].endswith(".csv") == False:
            exit("Not a CSV file")
    except FileNotFoundError:
        exit("File does not exist")


def read_write_file():
    with open(argv[2], "w") as file1:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(file1, fieldnames=fieldnames)
        writer.writeheader()
        with open(argv[1]) as file:
            reader = csv.reader(file)
            count = 0
            for row in reader:
                if count == 0:
                    count = count + 1
                    continue
                else:
                    name = row[0].strip('"').strip(" ")
                    last, first = name.split(",")
                    first = first.strip()
                    house = row[1]
                    writer.writerow({"first": first, "last": last, "house": house})
    file1.close()


main()
