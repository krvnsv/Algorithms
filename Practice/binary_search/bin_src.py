def bins(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2

    if arr[mid] == target:
        return arr[mid]
    elif arr[mid] > target:
        return bins(arr, target, left, mid - 1)
    else:
        return bins(arr, target, mid + 1, right)

arr = [1, 6, 3, 22, 9, 7, 5, 3, 0]
target = 22

arr.sort()  # Important: binary search requires a sorted array

print(bins(arr, target, 0, len(arr) - 1))
