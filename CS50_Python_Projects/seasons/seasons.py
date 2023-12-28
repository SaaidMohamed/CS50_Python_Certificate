from datetime import date, datetime
import inflect
import sys


def main():
    inpt_date_str = input("Date of Birth: ")
    inpt_date_str = inpt_date_str.strip()
    print(convert_to_words(get_minutes(inpt_date_str)))


def get_minutes(date_inpt):
    today_date = date.today()
    try:
        str_date = date_inpt
        format_date = "%Y-%m-%d"
        formated_date = datetime.strptime(str_date, format_date).date()
        delta_time = today_date - formated_date
        return round(int(delta_time.days) * 24 * 60)
    except ValueError:
        sys.exit("Invalid Date")


def convert_to_words(int_words):
    inf_p = inflect.engine()
    num_to_words = inf_p.number_to_words(int_words, andword="")
    return f"{num_to_words.capitalize()} minutes"


if __name__ == "__main__":
    main()
