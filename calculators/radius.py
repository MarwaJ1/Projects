#Function that determentns radius of a cone, globe and cylinder by using the height nad volym 
import math

# Cylinder = 3.14 * r**2 * h = V
# Cone = 3.14 * r**2 * h / 3 = v
# Globe = 3.14 * r**3 / 4/3
def get_radius(v, object, h=0):

    if object.lower() == "cylinder": 
        temp = v / 3.14 / h 
        radius = math.sqrt(temp)
        return radius 
    
    elif object.lower() == "cone": 
        temp = v /3.14 / h * 3
        radius = math.sqrt(temp)
        return radius
    
    elif object.lower() == "globe": 
        temp = v / 3.14 / 1.33
        radius = temp ** (1/3)
        return radius

# Testing 
print(get_radius(7000000000, "cylinder", 2))
print(get_radius(8.38, "cone", 2))
print(get_radius(67, "globe"))


    

