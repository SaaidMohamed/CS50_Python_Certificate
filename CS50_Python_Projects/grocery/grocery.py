def main():

    get_dict()



def get_dict():


    dicton = {}

    while True:

        try:
            item = input("").strip().upper()
            if item not in dicton.keys():
                dicton[item] = 1
            elif item in dicton.keys():
                dicton[item] = dicton[item] + 1


        except EOFError:

            try:
                for i in sorted(dicton.keys()):
                    print(dicton[i], i, sep=" ")
                break
            except:
                break


main()