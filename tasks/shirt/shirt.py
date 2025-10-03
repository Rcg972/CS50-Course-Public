import sys
from PIL import Image, ImageOps
import os

def main():
    extensi = [".jpeg", ".jpg", ".png"]
    if len(sys.argv) == 3:
        _, extensi_file_1 = os.path.splitext(sys.argv[1])
        _, extensi_file_2 = os.path.splitext(sys.argv[2])
        if extensi_file_1.lower() not in extensi or extensi_file_2.lower() not in extensi:
            sys.exit("Invalid output")
        else:
            if extensi_file_1.lower() == extensi_file_2.lower():
                try:
                    overlay(sys.argv[1],sys.argv[2])
                except FileNotFoundError:
                    sys.exit("Input does not exist")
            else:
                sys.exit("Input and output have different extensions")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")


def overlay(background, hasil):
    baju = Image.open("shirt.png")
    background = Image.open(background)
    background = ImageOps.fit(background, baju.size)
    background.paste(baju, (0, 0), baju)
    background.save(hasil)



if __name__ == "__main__":
    main()
