n = input("Expression: ")
x, y, z = n.split(" ")

match y:
    case "+":
        print(float(int(x) + int(z)))
    case "-":
        print(float(int(x) - int(z)))
    case "*":
        print(float(int(x) * int(z)))
    case "/":
        print(round((float(int(x) / int(z))),1))