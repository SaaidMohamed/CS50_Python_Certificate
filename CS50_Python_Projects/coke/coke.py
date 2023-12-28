amount_due = 50
print(f"Amount Due: {amount_due}")
cents = int(input("Insert Coin: "))

while True:

    if cents == 25 or cents == 10 or cents == 5:
        if amount_due != 0:
            amount_due = amount_due - cents
            if amount_due == 0:
                print(f"Change Owed: {amount_due}")
                break
            elif amount_due < 0:
                print(f"Change Owed: {amount_due *-1}")
                break
            print(f"Amount Due: {amount_due}")
            cents = int(input("Insert Coin: "))


    if cents != 25 and cents != 10 and cents != 5:
        print(f"Amount Due: {amount_due}")
        cents = int(input("Insert Coin: "))

