def main():

     print(run_code())


def run_code():
    while True:

        fraction_Inpt = input("Fraction: ").strip()
        return gauge(convert(fraction_Inpt))


def convert(fraction):
    try:
        first_int ,second_int = fraction.split("/")
        first_int = int(first_int)
        second_int = int(second_int)
        if first_int > second_int:
           run_code()
           return

        fraction_result = round((first_int / second_int) * 100)
        return fraction_result

    except (ValueError, ZeroDivisionError):
        run_code()
        return





def gauge(percentage):

    if percentage >=0 and percentage <= 1:
        percentage = "E"
        return percentage

    elif percentage >= 99 and percentage <= 100:
        percentage = "F"
        return percentage

    elif percentage > 1 and percentage < 99:
        return f"{percentage}%"

    else:
        return "Z%"


if __name__ == "__main__":
    main()

