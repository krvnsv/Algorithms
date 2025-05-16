# procedure binarySearch(list, key): 

#     start := 0 
#     end := len(list) - 1 
    
#     while start < end: 
#         mid_point = (start  + end ) // 2 
        
#         if key < list[mid_point]: 
#             end := mid_point - 1 
#         elseif key > list[mid_point]: 
#             start := mid_point + 1 
#         else: 
#             return mid_point 
#    end while 
# end procdeure

def binarySearch(our_list, key): 
    start = 0 
    end = len(our_list) - 1 
    midPoint = 0 
    
    while start <= end: 
        midPoint = (start + end) // 2 
        
        if our_list[midPoint] < key: 
            start = midPoint + 1 
        elif our_list[midPoint] > key: 
            end = midPoint - 1 
        else: 
            return key 
    return -1

