from sys import argv, exit
import csv
from tabulate import tabulate


def main():
    check_argv()

    with open(argv[1]) as file:
        reader = csv.reader(file)
        table_data_list = []
        count = 0
        for row in reader:
            if count == 0:
                keys = row
            else:
                table_data_list.append(row)
            count = count + 1

    print(make_table(table_data_list, keys))


def check_argv():
    if len(argv) == 1:
        exit("Too few command_line arguments")
    if len(argv) > 2:
        exit("Too many command_line arguments")
    try:
        if argv[1].endswith(".csv") == False:
            exit("Not a CSV file")
    except FileNotFoundError:
        exit("File does not exist")


def make_table(tablelist, headerss):
    table = tablelist
    headers = headerss
    return tabulate(table, headers, tablefmt="grid")


main()
