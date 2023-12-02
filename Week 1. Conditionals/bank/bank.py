n = input("Greeting: ")
if n.lower().strip()[0:5] == "hello":
    print("$0")
elif n.lower().strip()[0] == "h":
    print("$20")
else:
    print("$100")