import re

def main():
    print(convert(input("Hours: ")))

import re

def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.match(pattern, s)
    if not match:
        raise ValueError

    jam1, menit1, periode1, jam2, menit2, periode2 = match.groups()
    hasil = []

    for jam, menit, periode in [(jam1, menit1, periode1), (jam2, menit2, periode2)]:
        jam = int(jam)
        menit = int(menit) if menit else 0

        if not 1 <= jam <= 12:
            raise ValueError
        if not 0 <= menit < 60:
            raise ValueError

        if periode == "AM":
            if jam == 12:
                jam = 0
        elif periode == "PM":
            if jam != 12:
                jam += 12

        hasil.append(f"{jam:02}:{menit:02}")

    return f"{hasil[0]} to {hasil[1]}"


if __name__ == "__main__":
    main()
