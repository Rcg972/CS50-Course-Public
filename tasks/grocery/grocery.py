dict = {}

def main():
    while True:
        try:
            masukkan()
        except EOFError:
            print()
            print()
            keluaran()
            break


def masukkan():
    while True:
        item = input().strip().lower()
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1

def keluaran():
    for i in sorted(dict):
        print(f"{dict[i]} {i.upper()}")

main()
