def main():
    coke()


def coke():
    cents = (25, 10, 5)
    amount_due = 50
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))
        if coin in cents:
            amount_due -= coin
        else:
            continue
    print(f"Change Owed: {abs(amount_due)}")


main()
