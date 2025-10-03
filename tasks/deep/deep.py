def main():
    deep(input("What is the Answer to the Great Question of Life, the Universe, and Everything? : "))




def deep(x):
    x = x.strip().lower()
    if x == "42" or x == "forty-two" or x == "forty two":
        print("Yes")
    else:
        print ("No")


main()
