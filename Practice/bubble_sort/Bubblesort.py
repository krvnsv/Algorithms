def bubbleSort(arr):
    n = len(arr)

    for i in range (n):
        swapped = False

        for j in range (0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

arr = [12, 1, 11, 2, 13, 3, 14, 4]
print("Original list", arr)
bubbleSort(arr)
print("Sorted list", arr)