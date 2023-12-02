def main():
    x= input("What is the answer to the Great Question of Life, the Universe and Everything? ")
    match shorten(x):
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")

def shorten(y):
    y = y.lower().strip()
    return y

main()