def main():

    get_total()



def get_total():
    taqueria_menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    Total = 0

    while True:

        try:
            item = input("Item: ").strip().title()
            for k in taqueria_menu:
                if item == k:
                    Total = Total + taqueria_menu[k]
                    results = f"Total: ${Total :.2f}"
                    print(results)
        except EOFError:

            try:
                print(results)
                break
            except:
                break


main()