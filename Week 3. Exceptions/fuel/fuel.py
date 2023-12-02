def main():
    get_fraction("Fraction: ")

def get_fraction(prompt):
    while True:
        try:
            n = input(prompt)
            x, y = n.split("/")
            result = round(100 * int (x) / int (y))
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            if result > 100:
                pass
            elif result <= 1:
                print("E")
                break
            elif result >= 99:
                print("F")
                break
            else:
                print(str(int(result))+"%")
                break

main()
