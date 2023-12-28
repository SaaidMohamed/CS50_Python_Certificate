def main():
    Exp_input = input("Expression: ")
    Exp_input = Exp_input.strip()
    expression(Exp_input)

def expression(stranswer):
    if "+" in stranswer:
        sign_index = stranswer.index("+")
        first_value = int(stranswer[:sign_index])
        second_value = int(stranswer[sign_index + 1:])
        result = float(first_value + second_value)
        print(f"{result:.1f}")

    if "-" in stranswer:
        sign_index = stranswer.index("-")
        first_value = int(stranswer[:sign_index])
        second_value = int(stranswer[sign_index + 1:])
        result = float(first_value - second_value)
        print(f"{result:.1f}")

    if "/" in stranswer:
        sign_index = stranswer.index("/")
        first_value = int(stranswer[:sign_index])
        second_value = int(stranswer[sign_index + 1:])
        result = float(first_value / second_value)
        print(f"{result:.1f}")


    if "*" in stranswer :
        sign_index = stranswer.index("*")
        first_value = int(stranswer[:sign_index])
        second_value = int(stranswer[sign_index + 1:])
        result = float(first_value * second_value)
        print(f"{result:.1f}")



main()