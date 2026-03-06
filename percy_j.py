class Node: 

    def __init__(self, node_value=None, link_node=None): 
        self.node_value = node_value
        self.link_node = link_node 
    
    def get_value(self): 
        return self.link_value 
    
    def get_link_node(self): 
        return self.link_node 
    
    def set_link_node(self, link_node): 
        self.link_node = link_node

class PercyJacksonCharecter(Node): 
    def __init__(self, player, god=None, magical_item=None, power=None): 
        self.player = player
        self.god = god 
        self.magical_item = magical_item 
        self.power = power 

    def fighting_sim(self, monster, m_xp, p_xp): 
        player_name = input("Chose your player; either Annabeth or Percy")
        if player_name not in self.player: 
            print(f"Add a real player!! {self.player}")
        else: 
            print(f"Your {player_name} has {p_xp}!!!")
            if p_xp < m_xp: 
               help_player = input("Oh no!!! You have less strength then the monster, chose someone to help!!")

    def __str__(self): 
        return f"Name: {self.player}, Parent: {self.god}, Magical item : {self.magical_item} Power: {self.power}"

    
    
annabeth = PercyJacksonCharecter("Annabeth", "Athena", "Invisiblility cap")
print(annabeth)
    
annabeth.fighting_sim("Scylla", 2000, 6000)
