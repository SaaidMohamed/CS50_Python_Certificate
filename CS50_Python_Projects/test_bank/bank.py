def main():
    Greeting_input = input("Greeting: ")
    Greeting_input = Greeting_input.lower().strip()
    print(value(Greeting_input))

def value(stranswer):
    if stranswer.startswith("hello"):
        return 0
    elif  stranswer.startswith("h") :
        return 20
    else:
        return 100
if __name__ == "__main__":
    main()