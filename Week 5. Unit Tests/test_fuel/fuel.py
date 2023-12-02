def main():
    n = input("Fraction: ")
    print(gauge(convert(n)))

def convert(n):
    x, y = n.split("/")
    if int(x)/int(y) > 1:
        raise ValueError
    elif y == 0:
        raise ZeroDivisionError

    return int(100 * int(x) / int(y))


def gauge(percentage):
    if percentage <= 1:
         return "E"
    elif percentage >= 99:
         return "F"
    else:
         return f"{percentage}%"


if __name__ == "__main__":
    main()
