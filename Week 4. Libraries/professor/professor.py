import random


def main():
    score = 10
    level = get_level()
    for _ in range(10):
        numberList = generate_integer(level)
        for i in [0,1,2]:
            answer = int(input(f"{numberList[0]} + {numberList[1]} = "))
            if answer == (numberList[0]+numberList[1]):
                break
            else:
                print("EEE")
                if i == 2:
                    print(f"{numberList[0]} + {numberList[1]} =", (numberList[0]+numberList[1]))
                    score = score - 1

    print("Score: ", score)



def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        else:
            if level in [1,2,3]:
                return level
            else:
                continue


def generate_integer(level):
    numberList = []
    if level == 1:
        for _ in range(2):
            numberList.append(random.randint(0,9))
    elif level == 2:
        for _ in range(2):
            numberList.append(random.randint(10,99))
    else:
        for _ in range(2):
            numberList.append(random.randint(100,999))
    return numberList



if __name__ == "__main__":
    main()