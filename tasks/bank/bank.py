def main():
    bank(input("Greeting : "))



def bank(promt):
    if promt.strip().lower().startswith("h"):
        if promt.strip().lower().startswith("hello"):
            print("$0")
        else:
            print("$20")
    else:
        print("$100")



main()
