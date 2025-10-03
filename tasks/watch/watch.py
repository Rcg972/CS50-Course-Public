import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r"https?://(?:www\.)?youtube\.com/embed/([a-z0-9]+)"
    if "<iframe" and "></iframe>" in s:
        match = re.search(pattern, s, re.IGNORECASE)
    else:
        return None

    if match:
        last_word = match.group(1)
        return f"https://youtu.be/{last_word}"
    else:
        return None




if __name__ == "__main__":
    main()
