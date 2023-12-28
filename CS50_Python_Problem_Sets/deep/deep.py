def main():
    Qinput = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    Qinput = Qinput.lower().strip()
    deep_thoght(Qinput)

def deep_thoght(stranswer):
    match stranswer:
        case "42" | "forty-two"| "forty two":
            print("Yes")
        case _:
            print("No")

main()