def main():
    time = input("What time is it? ")
    time = time.strip()
    convert(time)
    meal_time(convert(time))



def convert(time):
    hours, minutes = time.split(":")
    result = (int(hours) * 3600 + int(minutes) * 60) / 3600
    return float(result)



def meal_time(Fn_value):
    if ( Fn_value >= 18 and Fn_value <= 19 ):
        print("dinner time")

    elif ( Fn_value >= 12 and Fn_value <= 13 ):
        print("lunch time")

    elif ( Fn_value >= 7 and Fn_value <= 8 ):
        print("breakfast time")



if __name__ == "__main__":
    main()
