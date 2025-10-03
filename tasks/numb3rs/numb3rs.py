import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    regex_ip = r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$"
    regex_ip = re.compile(regex_ip)
    if regex_ip.search(ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
