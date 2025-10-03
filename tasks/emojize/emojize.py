import emoji


def main():
    emojize(input("Input: "))




def emojize(inputan):
    print(emoji.emojize(inputan, language = "alias"))



if __name__ == "__main__":
    main()

