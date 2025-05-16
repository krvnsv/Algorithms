def partition(list, start, end):
    pivot = list[end]
    i = start - 1
    for j in range(start, end):
        if list[j] <= pivot:
            i += 1
            list[i], list[j] = list[j], list[i]
    list[i + 1], list[end] = list[end], list[i + 1]
    return i + 1

def quickSort(list, start, end):
    if start < end:
        pivot = partition(list, start, end)
        quickSort(list, start, pivot - 1)
        quickSort(list, pivot + 1, end)

arr = [12, 1, 11, 2, 13, 3, 14, 4]
print("Original list", arr)
quickSort(arr, 0, len(arr) - 1)
print("Sorted list", arr)
