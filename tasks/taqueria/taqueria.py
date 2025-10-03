def main():
    dict = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    Total = 0.00

    while True:
        try:
            Item = input("Item: ")
            Item = Item.title()
            if Item not in dict:
                continue
            else:
                Total += dict[Item]
                print(f"Total: ${Total:.2f}")
        except EOFError:
            print()
            break
        except KeyError:
            continue





main()
