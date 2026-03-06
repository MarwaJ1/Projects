# Calculating the volume that x persons head has in centiliter 
# Globe formula V = r**3 * pi * 3/4 

import math
def head_calc(radius): 
    volume = 4/3 * (radius**3 * math.pi)
    print(f"Your heads volume is {math.ceil(volume)} cm³")
    if volume > 1500: 
        print("YIKESSSS")
    else: 
      print("Alr not THAT big, seaweed brain.")
    brain_v = volume / 3
    print(f"Your brains total volume is {math.ceil(brain_v)} cm³")

#Testing 
head_calc(7) # Ungefär 2145 cm³ 

