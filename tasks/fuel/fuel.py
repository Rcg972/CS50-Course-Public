def main():
    hasil = fuel()
    if hasil <= 1:
        print("E")
    elif hasil >= 99:
        print("F")
    else:
        print(f"{hasil}%")



def fuel():
    while True :
        try:
            x,y = input("Fraction: ").split("/")
            if "." in x or "." in y:
                continue
            x = float(x)
            y = float(y)
        except (ValueError, ZeroDivisionError):
            continue
        else:
            if x < 0 or y == 0 or x>y:
                continue
            else:
                return int(round(x*100/y))




main()
