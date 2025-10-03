import inflect

p = inflect.engine()


def main():
    names = []
    try:
        while True:
            inputan = input("Name: ")
            names.append(inputan)
    except EOFError:
        adieu(names)


def adieu(names):
    hasil = p.join(names)
    print(f"Adieu, adieu, to {hasil}")


main()
