def main():
    n1 = str(input("please input the sentance: "))
    print(convert(n1))

def convert(n2):
    n2 = n2.replace(":)", "🙂")
    n2 = n2.replace(":(", "🙁")
    return n2

main()