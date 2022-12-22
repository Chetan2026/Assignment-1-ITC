import math as m
for i in range(0,346,15):
    s=m.radians(i)
    print(round(m.sin(s),4),"     ",round(m.cos(s),4))
