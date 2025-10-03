import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".csv"):
            print(tabulate(print_menu(sys.argv[1]), headers="keys", tablefmt="grid"))
        else:
            sys.exit("Not a CSV file")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")


def print_menu(x):
    with open(x, newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)   # ubah ke list supaya bisa dipakai tabulate


if __name__ == "__main__":
    main()
