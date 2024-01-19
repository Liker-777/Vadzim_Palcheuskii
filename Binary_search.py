def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = round((low + high) / 2)
        quess = list[mid]
        if quess == item:
            return mid
        if quess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


my_list = [int(i) for i in range(100)]
print(binary_search(my_list, 34))
