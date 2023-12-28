from random import randint
from sys import exit


def main():
    generate_integer(get_level())


def get_level():
    while True:
        level = input("Level: ").strip()
        if level.isnumeric():
            level = int(level)
            if 1<= level <=3:
                return level
            else:
                pass
        else:
            pass


def generate_integer(level):
    count = 0
    result = 0

    while count < 10:
        if level == 1:
            first_num = randint(0, 9)
            second_num = randint(0, 9)
        else:
            first_num = randint(int('1'+'0'*(level-1)), int('9'*level))
            second_num = randint(int('1'+'0'*(level-1)), int('9'*level))

        equation = input(f"{first_num} + {second_num} = ").strip()

        if equation.isnumeric():
            equation = int(equation)
            sum = first_num + second_num

            if equation == sum :
                result = result + 1
                pass
            elif equation != sum:
                print("EEE")
                n_count = 0

                while equation != sum and n_count<2:
                    equation = input(f"{first_num} + {second_num} = ").strip()

                    if equation.isnumeric():
                        equation = int(equation)
                        if equation == sum :
                            result = result + 1
                        elif equation != sum:
                            print("EEE")
                    n_count = n_count + 1
                if n_count == 2:
                    print(f"{first_num} + {second_num} = {sum}")

                pass

        count = count + 1

    print(f"Score: {result}")


if __name__ == "__main__" :
    main()
