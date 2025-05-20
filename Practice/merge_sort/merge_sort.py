# 1. Step divide list in two halfs 
# 2. Sort both halfs 
# 3. Merge sorted parts


# procedure MergeSort(list as list_of_elements)Do 
#     len = len(list) 
#     if len == 1 Then Stop 
    
#     left :[] 
#     right :[] 
    
#     for i := 1 to len//2 Do 
#         left.append(list[i]) 
#         right.append(list[len // 2 + i]) 
#     end for 
    
#      MergeSort(left) 
#      MergeSort(right) 
     
#      list:= Merge(left, right) 
# end procedure


def MergeSort(ourList): 
    if len(ourList) > 1: 
        left = ourList[:len(ourList)// 2] 
        right = ourList[len(ourList)// 2:] 
        MergeSort(left) 
        MergeSort(right) 
        Merge(left, right, ourList)


def Merge(left, right, ourList): 
    i = j = k = 0 
    
    while i < len(left) and j < len(right): 
        if left[i] <= right[j]: 
            ourList[k] = left[i] 
            i += 1 
        else: 
            ourList[k] = right[j] 
            j += 1 
        k += 1 
        
    
    while i < len(left): 
        ourList[k] = left[i]
        i += 1 
        k += 1 
    while j < len(right): 
        ourList[k] = right[j]
        j += 1 
        k += 1 


ourList = [3,25,15,21,23,1] 
print(ourList) 
MergeSort(ourList) 
print(ourList)