import sys
import csv


def main():
    if len(sys.argv) == 3:
        if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
            data_before = baca_data(sys.argv[1])
            tulis_data(sys.argv[2], data_before)
        else:
            sys.exit("Not a CSV file")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")


def baca_data(before):
    with open(before, newline = "") as before_file:
        reader = csv.DictReader(before_file)
        new_data = []
        for data in reader:
            last, first = data['name'].split(",")
            first = first.strip()
            last = last.strip()
            new_dict = {
                "first" : first,
                "last" : last,
                "house" : data['house']
            }
            new_data.append(new_dict)

        return new_data

def tulis_data(after, data):
    with open(after, "w", newline = "") as after_file:
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(after_file, fieldnames = fieldnames)

        writer.writeheader()
        writer.writerows(data)



if __name__ == "__main__":
    main()
