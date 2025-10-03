def main():
    twttr(input("Input: "))


def twttr(promt):
    vokal = ("a", "i" ,"u", "e", "o", "A", "I", "U", "E" ,"O")
    result = ""
    for huruf in promt:
        if huruf not in vokal:
            result += huruf

    print(result)






main()
