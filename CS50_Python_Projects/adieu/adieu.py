
import inflect
from sys import exit

p = inflect.engine()
names_list = []
while True:
    try:
        inpt = input("Name: ")
        names_list.append(inpt)

    except EOFError:
        mylist = p.join(names_list)
        print(f"Adieu, adieu, to {mylist}")
        exit()
