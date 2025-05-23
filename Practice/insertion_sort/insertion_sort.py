# procedure InsertSort(list as list of numbers): 
#     len:= len(list) - size of list / number of elements 
#     for i:= 2 to len: 
#         j:= i 
#         while j > 1 and list[j] < list[j - 1]: 
#             swap(list[j], list[j - 1]) 
#             j:= j - 1 
#         end while 
#     end for 
# end procedure

def insertSort(our_list): 
    n = len(our_list) 
    
    for i in range(1, n): 
        key = our_list[i] 
        j = i - 1 
        
        while j >= 0 and our_list[j] > key: 
            our_list[j + 1] = our_list[j] 
            j -= 1 
        our_list[j + 1] = key

ourList = [12,1,11,2,13,3,14,4] 
print("Original list", ourList) 
insertSort(ourList)
print("Sorted list", ourList)