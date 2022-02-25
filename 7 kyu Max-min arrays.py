def solve(arr):
    arr_copy = arr[:]
    lst = []

    while arr_copy:
        lst.append(max(arr_copy))
        del arr_copy[arr_copy.index(max(arr_copy))]
        if arr_copy:
            lst.append(min(arr_copy))
            del arr_copy[arr_copy.index(min(arr_copy))]

    return lst


print(solve([15, 11, 10, 7, 12]), [15, 7, 12, 10, 11])
print(solve([91, 75, 86, 14, 82]), [91, 14, 86, 75, 82])
print(solve([84, 79, 76, 61, 78]), [84, 61, 79, 76, 78])
print(solve([52, 77, 72, 44, 74, 76, 40]), [77, 40, 76, 44, 74, 52, 72])
print(solve([1, 6, 9, 4, 3, 7, 8, 2]), [9, 1, 8, 2, 7, 3, 6, 4])
print(solve([78, 79, 52, 87, 16, 74, 31, 63, 80]), [87, 16, 80, 31, 79, 52, 78, 63, 74])
