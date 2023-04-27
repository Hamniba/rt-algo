def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high)/2)
        num = list[mid]
        if num == item:
            return mid
        elif num > item:
            high = mid - 1
        else:
            low = mid + 1

    return None

my_list = [1, 4, 6, 11, 26, 310]
print(binary_search(my_list, 4))
print(binary_search(my_list, 26))
