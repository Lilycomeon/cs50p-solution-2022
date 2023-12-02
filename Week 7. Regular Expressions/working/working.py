import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"([1-9]|1[0-2]):?([0-5][0-9])? (AM|PM) to ([1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)", s):
        stattime1 = int(matches.group(1))
        stattime2 = matches.group(2)
        statperiod = matches.group(3)
        endtime1 = int(matches.group(4))
        endtime2 = matches.group(5)
        endperiod = matches.group(6)
        if stattime2 == None:
            stattime2 = "00"
        if endtime2 == None:
            endtime2 = "00"
        if statperiod == "AM" and stattime1 == 12:
            stattime1 = 0
        if endperiod == "AM" and endtime1 == 12:
            endtime1 = 0
        if statperiod == "PM" and stattime1 != 12:
            stattime1 = stattime1 + 12
        if endperiod == "PM" and endtime1 != 12:
            endtime1 = endtime1 + 12
        return (f"{stattime1:02}:{stattime2} to {endtime1:02}:{endtime2}")
    else:
        raise ValueError




if __name__ == "__main__":
    main()