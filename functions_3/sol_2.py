# Function returning multiple values.
import math

def circle(radius):
   area=  math.pi * radius ** 2
   circum=2*math.pi*radius
   return area,circum
result=circle(5)
print(result)