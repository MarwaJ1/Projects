class Node: 
    def __init__(self, value=None, link_node=None):
        self.value = value 
        self.link_node = link_node 
    
    def get_value(self): 
        return self.value 
    
    def get_link_node(self): 
        return self.link_node
    
    def set_link_node(self, link_node): 
        self.link_node = link_node #Overwriting 
    
    #Strigifying it : 
    def __str__(self): 
        return f"This node has the value: {self.value}"

#Testing 

x = Node(23)
y = Node(32)
z = Node(1)

x.set_link_node(y)
y.set_link_node(z) # z will be the last node!
print(x, y, z)
    