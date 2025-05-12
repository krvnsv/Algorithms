def selectionSort(our_list):
    n = len(our_list)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if our_list[j] < our_list[min_index]:
                min_index = j
        our_list[i], our_list[min_index] = our_list[min_index], our_list[i]

our_list = [12,1,11,2,13,3,14,4]
print("Original list", our_list)
selectionSort(our_list)
print("Sorted list", our_list)