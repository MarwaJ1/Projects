from linkedlist import Node

class Stack: 

    def __init__(self, limit=1000): 
        top_item = None 
        self.size = 0 
        self.limit = limit 
    
    def has_space(self): 
        return self.limit > self.size
    
    def is_empty(self): 
        return self.size == 0 
    
    def peek(self): 
        if not self.is_empty():
            return self.top_item.get_value() 
        else: 
            print("This stack is empty!")
    
    def pop(self): 
        if not self.is_empty(): 
            item_to_remove = self.top_item 
            self.top_item = self.top_item.get_link_node()
            self.size -= 1
            print("Removing stack...")
        else: 
            print("This stack is empty!")

    def push(self, value): 
        if self.has_space(): 
            new_item = Node(value)
            new_item.set_next_node(self.top_item)
            size += 1
        else: 
            print("This stack is full!")


spotify = Stack() 

spotify.push("Fire to the rain")
print(spotify.get_value())
