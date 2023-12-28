def main():
    print(get_value())


def get_value():

    while True:

        try:
            fraction_Inpt = input("Fraction: ").strip()
            first_int ,second_int = fraction_Inpt.split("/")

            first_int = int(first_int)
            second_int = int(second_int)

            fraction_result = round(first_int / second_int * 100)

            if fraction_result <= 1:
                fraction_result = "E"
                return fraction_result

            elif fraction_result >= 99 and fraction_result <= 100:
                fraction_result = "F"
                return fraction_result

            if fraction_result > 100 :
                fraction_result = 1/0

            fraction_result = f"{fraction_result}%"
            return fraction_result


        except (ValueError, ZeroDivisionError):
            pass



main()


