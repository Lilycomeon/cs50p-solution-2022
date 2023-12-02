def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #start with at least two letters
    if not s[0:2].isalpha():
        return False

    #a maximum of 6 characters and a minimum of 2 characters
    if not 2 <= len(s) <= 6:
        return False

    #The first number used cannot be a ‘0’.
    for c in s:
        if c.isdigit() and c == "0":
            return False
        elif c.isdigit():
            break

    #numbers must come at the end
    index = 0
    for c in s:
        index = index + 1
        if c.isdigit():
            break

    for c in s[index+1:len(s)]:
        if c.isalpha():
            return False

    #No periods, spaces, or punctuation marks are allowed
    for c in s:
        if not (c.isalpha() or c.isdigit()):
            return False

    return True

if __name__ == "__main__":
    main()