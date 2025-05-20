def binarySearch(ourList, start, end, key): 
    
    mid = (start + end) // 2 
    if ourList[mid] == key: 
        return mid 
    elif ourList[mid] > key: 
        return binarySearch(ourList, start, mid - 1, key) 
    else: 
        return binarySearch(ourList, mid + 1, end, key) 
    

ourList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14] 
key = 10 
r= binarySearch(ourList, 0, len(ourList) - 1, key) 
print("Element is on index ", r)