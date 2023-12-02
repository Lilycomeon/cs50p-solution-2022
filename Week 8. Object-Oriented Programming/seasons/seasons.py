from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    bdate = input("Date of Birth: ")
    try:
        year, month, day = check_birthday(bdate)
    except:
        sys.exit("Invalid Date")
    else:
        bdate = date(int(year), int(month), int(day))
        todate = date.today()
        diff = todate - bdate
        minutes = diff.days * 24 * 60
        minutes_words = p.number_to_words(minutes, andword="")
        print(minutes_words.capitalize() + " minutes")

def check_birthday(bdate):
    if date.fromisoformat(bdate):
        year, month, day = bdate.split("-")
        return year, month, day

if __name__ == "__main__":
    main()