def flatten_and_sort(array):
    lst = []

    for i in array:
        lst += i

    return sorted(lst)


print(flatten_and_sort([]), [])
print(flatten_and_sort([[], []]), [])
print(flatten_and_sort([[], [1]]), [1])
print(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(flatten_and_sort([[1, 3, 5], [100], [2, 4, 6]]), [1, 2, 3, 4, 5, 6, 100])
