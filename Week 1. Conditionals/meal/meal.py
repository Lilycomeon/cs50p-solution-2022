def main():
    time = input("What time is it? ")

    if 7 <= convert(time) <= 9:
        print("breakfast time")
    elif 12 <= convert(time) <= 13:
        print("lunch time")
    elif 18 <= convert(time) <= 19:
        print("dinner time")


def convert(time):
    time = time.strip()
    hours, minutes = time.split(":")
    timme = float(hours) + float(minutes)/60
    return timme


if __name__ == "__main__":
    main()