def main():
    Greeting_input = input("Greeting: ")
    Greeting_input = Greeting_input.lower().strip()
    bank_pay(Greeting_input)

def bank_pay(stranswer):
    if stranswer.startswith("hello"):
        print("$0")
    elif  stranswer.startswith("h") :
        print("$20")
    else:
        print("$100")

main()