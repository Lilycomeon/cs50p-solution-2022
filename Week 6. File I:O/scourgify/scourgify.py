import sys
import csv

info = []

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    try:
        with open(sys.argv[1]) as file1:
            reader = csv.DictReader(file1)
            for row in reader:
                last,first = row["name"].split(",")
                info.append({"first": first.strip(), "last": last, "house": row["house"]})

        with open(sys.argv[2],"w") as file2:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(file2, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows(info)

    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")