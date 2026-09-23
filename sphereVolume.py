import math
pi_value = math.pi 

def sphere_volume (radius):
    volume = (4/3)*math.pi*radius**3
    return volume
print(f"The volume of the sphere is {sphere_volume(5)} cm^3.")
