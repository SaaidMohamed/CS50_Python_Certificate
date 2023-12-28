def main():

    get_dict()


def get_dict():

    months_list = [
                    "January",
                    "February",
                    "March",
                    "April",
                    "May",
                    "June",
                    "July",
                    "August",
                    "September",
                    "October",
                    "November",
                    "December"
                ]

    while True:

        try:

            date_inpt = input("Date: ").strip()

            if date_inpt[0].isalpha():
                MM, DD, YYYY = date_inpt.split(" ")
                MM = MM.title()

                if MM in months_list:
                    MM = months_list.index(MM) + 1
                    DD, jj = DD.split(",")
                    DD = int(DD)
                    if DD<0 or DD>=31:
                        continue
                    else:
                        standard_date = f"{int(YYYY)}-{int(MM):02}-{DD:02}"
                        print(standard_date)
                        break


            else:

                MM, DD, YYYY = date_inpt.split("/")
                MM = int(MM)
                DD = int(DD)
                YYYY = int(YYYY)
                if MM>12 or MM < 1 or DD<0 or DD>31:
                    continue
                else:
                    standard_date = f"{YYYY}-{MM:02}-{DD:02}"
                    print(standard_date)
                    break


        except EOFError:
            break

        except ValueError:
            continue


main()