from validator_collection import validators, checkers, errors


def main():
    print(validate_email(input("What's your email address? ")))


def validate_email(e_str):
    try:
        email_address = validators.email(e_str)
        if email_address == e_str:
            return "Valid"
        else:
            return "Invalid"

    except errors.EmptyValueError:
        return "Invalid"

    except errors.InvalidEmailError:
        return "Invalid"


if __name__ == "__main__":
    main()
