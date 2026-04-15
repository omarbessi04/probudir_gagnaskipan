def length_of_list(li: list[int]):
    if li == []:
        return 0
    return 1 + length_of_list(li[1:])


print(length_of_list([1, 2, 3]))
