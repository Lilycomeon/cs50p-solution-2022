import inflect

p = inflect.engine()

nameList = []
while True:
    try:
        name = input("Name: ")
        nameList.append(name)
    except EOFError:
        print()
        break
    else:
        continue

print("Adieu, adieu, to " + p.join(nameList))

