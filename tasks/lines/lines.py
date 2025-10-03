import sys


def main():
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".py"):
            print(count_LOC(sys.argv[1]))
        else:
            sys.exit("Not a Python file")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")



def count_LOC(x):
    count = 0
    try:
        with open(x) as file:
            for line in file:
                if line.rstrip() == "" or line.lstrip().startswith("#"):
                    continue
                else:
                    count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    return count



if __name__ == "__main__":
    main()
