import numpy as np
import math
n=int(input("number of coordinate required ::"))
a=np.empty((0,2),int)
b=np.empty((0,2),dtype=float)
i=0
while i<n:
    x=int(input("give x co-ordinate:"))
    y=int(input("give y co-ordinate:"))
    data=np.array([x,y])
    a=np.vstack([a,data])
    i+=1
j=0
while j<n :
    r = math.sqrt(a[j, 0] ** 2 + a[j, 1] ** 2)
    angle = math.degrees(math.atan2(a[j, 1], a[j, 0]))
    data = np.array([r, angle]) 
    b = np.vstack([b, data])
    j+=1
print("Cartesian Co-ordinates::")
print(a)
print("Polar Co-ordinates::")
print(b)
