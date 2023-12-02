def main():
    lists = get_list()
    lists.sort()

    for i in lists:
        count = 0
        for j in lists:
            if i == j:
                count = count + 1
                if count >= 2:
                    lists.remove(j)
        print(count, i)


def get_list():
    itemList = []
    while True:
        try:
            item = input().upper()
            itemList.append(item)
        except EOFError:
            break

    return itemList

main()