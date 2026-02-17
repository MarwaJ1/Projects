# Calculating the volume that x persons head has in centiliter 
# Globe formula V = r**3 * pi * 3/4 

import math
def head_calc(radius): 
    volume = 4/3 * (radius**3 * math.pi)
    print(f"Your heads volume is {math.ceil(volume)} cm³")

#Testing 
head_calc(8) # Ungefär 2145 cm³ 