class Node: 
    def __init__(self, data, next_p = None):
        self.data = data
        self.next_p = next_p



class singleLinkedList: 
    def __init__(self): 
        self.head = None 
        self.tail = None 
        self.size = 0 
    
    def __len__(self): 
        return self.size 
    
    def __iter__(self): 
        current = self.head 
        while current is not None: 
            yield current.data 
            current = current.next_p 
            
    def _iter_node(self): 
        
        current = self.head 
        while current is not None: 
            yield current
            current = current.next_p 
            

    def first(self): 
        if self.size == 0: 
            raise IndexError("List is empty") 
        return self.head.data 
    
    def last(self): 
        if self.size == 0: 
            raise IndexError("List is empty") 
        return self.tail.data 
    
            
    def show(self): 
        result = "[" 
        counter = 0 
        for element in self: 
            result += str(element) 
            if counter < len(self) - 1: 
                result += "->" 
            counter += 1 
        return result + "]" 
    
    def insertEnd(self, data): 
        
        new_node = Node(data) 
        
        if self.size == 0: 
            self.head = new_node 
        else: 
            self.tail.next_p = new_node 
        self.tail = new_node 
        self.size += 1 
    
    def insertStart(self, data): 
        
        new_node = Node(data, self.head) 
        if self.size == 0: 
            self.tail = new_node 
        self.head = new_node 
        self.size += 1 
        
    def remove_first(self): 
        
        if self.size == 0: 
            raise IndexError("Liste is empty")
            
        if self.size == 1: 
            self.head = self.tail = None
        self.head = self.head.next_p 
        self.size -= 1 
        if self.size == 0: 
            self.tail = None
            
    def remove_last(self): 
        
        if self.size == 0: 
            raise IndexError("Liste is empty")  
        if self.size == 1: 
            self.head = self.tail = None 
        else: 
            for node in self._iter_node(): 
                if node.next_p == self.tail: 
                    node.next_p = None 
                    self.tail = node 
                    break 
        self.size -= 1  
        
    def removeByValue(self, value): 
        
        if self.size == 0: 
            raise IndexError("Liste is empty") 
        if self.size == 1 and self[0] == value:
            self.head = self.tail = None
            self.size -= 1 
            return 
        counter = 0 
        prev = None 
        
        for node in self._iter_node(): 
            if node.data == value and counter == 0: 
                self.head = self.head.next_p 
                self.size -= 1 
                return 
            if node.data == value and counter == len(self) - 1: 
                self.tail = prev 
                prev.next_p = None 
                self.size -= 1 
                return 
            if node.data == value: 
                prev.next_p = node.next_p 
                self.size -= 1 
                return 
            prev = node 
            counter += 1 
        raise ValueError("There is no such element in list") 
        
        
    def removeByIndex(self, i = None): 
        if i is None: 
            i = self.size - 1 
        
        if not 0<= i and i < self.size: 
            raise IndexError("Out of bounds") 
            
        if self.size == 0: 
            raise IndexError("List is empty") 
            
        counter = 0
        prev = None 
        
        for node in self._iter_node(): 
            if i == counter == 0: 
                self.head = self.head.next_p 
                self.size -= 1 
                return 
            if i == counter == len(self.size) - 1: 
                self.tail = prev 
                prev.next_p = None 
                self.size -= 1 
                return  
            if i == counter: 
                prev.next_p = node.next_p 
                self.size -= 1 
                return 
            prev = node 
            counter += 1
        


if __name__ == '__main__': 
    linkedList = singleLinkedList() 
    linkedList.insertEnd(5) 
    linkedList.insertEnd(10)
    linkedList.insertEnd(15) 
    print(linkedList.show()) 
    linkedList.insertStart(50) 
    print(linkedList.show())  
    linkedList.remove_last()
    print(linkedList.show()) 
    linkedList.insertEnd(150) 
    linkedList.insertEnd(200)
    linkedList.insertEnd(250) 
    print(linkedList.show())  
    linkedList.removeByValue(200) 
    print(linkedList.show())  



class Car: 
    
    def __init__(self, brand, model, horsePower): 
        self.brand = brand 
        self.model = model 
        self.horsePower = horsePower 
        
    def __eq__(self, other): 
        if isinstance(other, Car): 
            if self.horsePower == other.horsePower: 
                return True 
            return False 
        
    def __ge__(self, other): 
        if isinstance(other, Car): 
            if self.horsePower >= other.horsePower: 
                return True 
            return False
        


linkedListCar = singleLinkedList()  
