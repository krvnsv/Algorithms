class Node: 
    def __init__(self, value, next_p = None): 
        self.value = value 
        self.next_p = next_p



class SingleLinkedList: 
    def __init__(self): 
        self.head = None 
        self.tail = None 
        self.size = 0 
        
    def __len__(self): 
        return self.size 
    
    def insert_end(self, value): 
        new_node = Node(value) 
        if self.size == 0: 
            self.head = new_node 
        else: 
            self.tail.next_p = new_node 
        self.tail = new_node 
        self.size += 1 
    def insert_start(self, value): 
        new_node = Node(value, self.head) 
        
        if self.size ==0: 
            self.tail = new_node 
        self.head = new_node 
        self.size += 1
        
    def remove_last(self): 
        if self.size == 0: 
            return 
        elif self.size == 1: 
            self.head = None 
            self.tail = None 
        else: 
            current = self.head 
            while current.next_p != self.tail: 
                current = current.next_p 
            current.next_p = None 
            self.tail = current 
        self.size -= 1 
        
    def remove_first(self): 
        if self.size == 0: 
            return 
        elif self.size == 1: 
            self.tail = None 
        self.head = self.head.next_p 
        self.size -= 1 
        
    def first(self): 
        if self.size ==0: 
            raise IndexError("List is empty") 
        return self.head.value 
    
    def last(self): 
        
        if self.size == 0: 
            raise IndexError("List is empty") 
        return self.tail.value 
    


class OurStack: 
    def __init__(self): 
        self.stack = SingleLinkedList()  
        
    def __len__(self): 
        return len(self.stack)
        
    def push(self, data): 
        self.stack.insert_end(data) 
        
    def pop(self): 
        
        try: 
            data = self.stack.last() 
            self.stack.remove_last() 
            return data 
        except:
            raise IndexError("Stack is empty")
        


class OurQueue: 
    def __init__(self): 
        self.queue = SingleLinkedList() 
    def __len__(self): 
        return len(self.queue) 
    
    def enQueue(self, data): 
        self.queue.insert_end(data) 
        
    def deQueue(self): 
        try: 
            data = self.queue.first() 
            self.queue.remove_first() 
            return data 
        except: 
            raise IndexError("Queue is empty") 
    def peek_front(self): 
        try: 
            return self.queue.first() 
        except: 
            raise IndexError("Queue is empty")