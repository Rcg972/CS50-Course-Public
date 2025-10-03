import random as rd


def main():
    while True:
        Level = input("Level: ")
        if not Level.isnumeric():
            continue
        Level = int(Level)
        if Level <= 0:
            continue
        tebak(Level)
        break



def tebak(Level):
    target = rd.randint(1, Level)
    while True:
        tebakan = input("Guess: ")
        if not tebakan.isnumeric():
            continue
        tebakan = int(tebakan)
        if tebakan <= 0:
            continue

        if tebakan > target:
            print("Too large!")
            continue
        elif tebakan < target:
            print("Too small!")
            continue
        else:
            print("Just right!")
            break


main()

