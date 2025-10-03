import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
list_font = figlet.getFonts()

def main():
    if len(sys.argv) == 1:
        ASCI_Art_Random()
    elif len(sys.argv) == 3:
        ASCI_Art()
    else:
        sys.exit(1)


def ASCI_Art_Random():
     inputan = input("Input: ")
     f = Figlet(font = random.choice(list_font))
     print(f.renderText(inputan))


def ASCI_Art():
    if sys.argv[1] not in ["-f", "--f"]:
        sys.exit(1)

    if sys.argv[2] not in list_font:
        sys.exit(1)

    f = Figlet(font = sys.argv[2])
    inputan = input("Input: ")
    print(f.renderText(inputan))


main()

