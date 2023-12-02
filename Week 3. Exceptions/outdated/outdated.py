def main():
    change_date("Date: ")


def change_date(prompt):
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    while True:
        oldDate = input(prompt)
        if "/" in oldDate:
            x, y, z = oldDate.split("/")
            try:
                x = int(x)
                y = int(y)
            except ValueError:
                continue
            else:
                if x > 12:
                    continue
                elif y > 31:
                    continue
                else:
                    date = ""
                    date = z.strip() + "-" + f"{x:02}" + "-" + f"{y:02}"
                    print(date)
                    break
        elif "," in oldDate:
            n, z = oldDate.split(",")
            x, y = n.split(" ")
            digitalmonth = ""

            if x not in months:
                continue
            elif int(y) > 31:
                continue
            else:
                for month in months:
                    if month == x:
                        digitalmonth = months[x]
                date = ""
                date = z.strip() + "-" + f"{int(digitalmonth):02}" + "-" + f"{int(y):02}"
                print(date)
                break

main()