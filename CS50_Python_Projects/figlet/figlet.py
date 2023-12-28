from sys import argv, exit
from pyfiglet import Figlet
from random import choice


figlet = Figlet()

if len(argv) < 2:

    inpt = input("Input: ")
    figlet.setFont(font=choice(figlet.getFonts()))
    print(f"Output: {figlet.renderText(inpt)}")

elif len(argv) < 3:

    exit("Example: python figlet.py -f or --font slant")

elif (argv[1]== "-f" or argv[1]== "--font") and argv[2] in figlet.getFonts() :

    inpt = input("Input: ")
    figlet.setFont(font= argv[2])
    print(f"Output: {figlet.renderText(inpt)}")

else:

    exit("Example: python figlet.py -f or --font slant")

