def main():
    initialAmount = 50
    print("Amount Due:", initialAmount)
    amount_due(initialAmount)

def get_coin(a):
    while True:
        c = int(input("Insert Coin: "))
        if c in [25, 10, 5]:
            break
        else:
            print("Amount Due:", a)
    return c

def amount_due(i):
    amount = i
    while amount > 0:
        coin = get_coin(amount)
        amount = amount - coin
        if amount > 0:
            print("Amount Due:", amount)
        else:
            print("Change Owed:", -amount)


main()
