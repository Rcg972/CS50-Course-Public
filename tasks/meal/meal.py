def main():
    hasil = convert(input("What time is it?  : "))
    if hasil <= 8.00 and hasil >= 7.00:
        print("breakfast time")
    elif hasil <= 13.00 and hasil >= 12.00:
        print("lunch time")
    elif hasil <= 19.00 and hasil >= 18.00:
        print("dinner time")


def convert(time):
    jam, menit = time.split(":")
    waktu = float(jam) + (float(menit)/60)
    return waktu



if __name__ == "__main__":
    main()
