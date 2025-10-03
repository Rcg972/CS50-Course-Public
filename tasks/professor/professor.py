import random as rd


def main():
    lvl = get_level()
    benar = 0
    for i in range(10):
        bil1 = generate_integer(lvl)
        bil2 = generate_integer(lvl)
        jawaban = bil1 + bil2

        percobaan = 0
        while percobaan < 3:
            try:
                User = int(input(f"{bil1} + {bil2} = "))
                if User == jawaban:
                    benar += 1
                    break
                else:
                    print("EEE")
                    percobaan +=1
            except ValueError:
                print("EEE")
                percobaan +=1

        if percobaan == 3:
            print(f"{bil1} + {bil2} = {jawaban}")



    print (f"Score: {benar}")


def get_level():
    while True:
        try:
            Level = int(input("Level: "))
            if Level > 3 or Level < 1:
                raise ValueError()
            else:
                return Level
        except ValueError:
            continue



def generate_integer(level):
    if level == 1:
        return rd.randint(0,9)
    elif level == 2:
        return rd.randint(10,99)
    elif level == 3:
        return rd.randint(100,999)


if __name__ == "__main__":
    main()
