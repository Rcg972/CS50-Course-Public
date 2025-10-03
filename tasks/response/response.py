from validator_collection import checkers


def main():
    print(email_checker(input("What's your email address? ")))


def email_checker(s):
    if checkers.is_email(s):
        return "Valid"
    else:
        return "Invalid"







if __name__ == "__main__":
    main()
