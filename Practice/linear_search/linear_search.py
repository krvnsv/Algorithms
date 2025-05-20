# procedure linearSearch(list, valueToSearch): 
#     for i from 0 to len(list) - 1: 
#         if list[i] == valueToSearch: 
#             return i - index whhere founded element is 
#         end if 
#     end for 
    
#     return -1 
# end procdeure 


def linearSearch(our_list, key): 
    for i in range(len(our_list)): 
        if our_list[i] == key: 
            return i 
    return -1