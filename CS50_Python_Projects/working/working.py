import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if len(s) < 11:
        raise ValueError("Invalid Value")

    def from_T(f_t_s):
        try:
            hour, minute, am_pm = re.findall(r"\d+|\w+", f_t_s)

            if int(minute) > 59 or am_pm == "00":
                raise ValueError("Invalid Value")

        except:
            hour, am_pm = re.findall(r"\d+|\w+", f_t_s)

        hour = int(hour)
        if int(hour) > 12 or am_pm == "00":
            raise ValueError("Invalid Value")
        if am_pm == "PM" and hour != 12:
            hour += 12
        elif am_pm == "AM" and hour == 12:
            hour = 0
        try:
            r_value = f"{hour:02d}:{minute}"

        except:
            r_value = f"{hour:02d}:00"

        return r_value

    def to_T(t_t_s):
        try:
            hour, minute, am_pm = re.findall(r"\d+|\w+", t_t_s)

            if int(minute) > 59 or am_pm == "00":
                raise ValueError("Invalid Value")

        except:
            hour, am_pm = re.findall(r"\d+|\w+", t_t_s)

        hour = int(hour)
        if int(hour) > 12 or am_pm == "00":
            raise ValueError("Invalid Value")
        if am_pm == "PM" and hour != 12:
            hour += 12
        elif am_pm == "AM" and hour == 12:
            hour = 0
        try:
            r_value = f"{hour:02d}:{minute}"
        except:
            r_value = f"{hour:02d}:00"

        return r_value

    try:
        from_time, to_time = s.split("to")
    except:
        s = s
        return f"{from_T(s)}:00"

    return f"{from_T(from_time)} to {to_T(to_time)}"


if __name__ == "__main__":
    main()
