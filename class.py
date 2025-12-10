class Node: 

    def __init__(self, value, link_node=None): 
        self.value = value 
        self.link_node = link_node 
    
    def get_value(self): 
        return self.value
    
    def get_link_node(self): 
        return self.link_node 
    
    def set_link_node(self, link_node): 
        self.link_ndoe = link_node

class LinkedList: 

    def __init__(self, value=None): 
        self.head_node = Node(value) 

    def get_head_node(self): 
        return self.head_node 
    
    def get_next_node(self): 
        pass
    
    def insert_begining(self, value): 
        new_head = Node(value)
        new_head.set_link_node(self.head_node)
        self.head_node = new_head 

    def strinify(self): 
        stringify = "" # Saving all of the nodes 
        current_node = self.get_head_node()

        while current_node: 
            if current_node.get_value() != None: 
                stringify += str(current_node.get_link_node()) + "\n"
            current_node = current_node.get_link_node()
        return stringify

    
    # removing (Garbage collecting) 

    def remove_node(self, value_to_remove): 
        current_node = self.get_head_node()
        next_node = current_node.get_link_ndoe() 
        
        if current_node.get_link_node().get_value() == value_to_remove: 
            next_node.get_link_node()
        
        else: 
            while current_node: 
                if current_node.get_link_node().get_value() == value_to_remove: 
                    current_node.set_link_node(current_node.get_link_node())
                    current_node = None

        
        




    