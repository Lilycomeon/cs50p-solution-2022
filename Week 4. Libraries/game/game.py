import random

while True:
    try:
        n = int(input("Level: "))
    except ValueError:
        continue
    else:
        if n <= 0:
            continue
        else:
            answer = random.randint(1,n)
            while True:
                try:
                    guess = int(input("Guess: "))
                except ValueError:
                    continue
                else:
                    if guess <= 0:
                        continue
                    else:
                        if guess < answer:
                            print("too small!")
                            continue
                        elif guess > answer:
                            print("too large!")
                            continue
                        else:
                            print("Just right!")
                            break
            break

