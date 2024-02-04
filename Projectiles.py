import math

theta = float(input())
v = float(input())
alpha = float(input())

t = (2 * v * math.sin(theta*3.14/180)) / (9.8 * math.cos(alpha*3.14/180))

OM = v * math.cos(theta*3.14/180) * t + 0.5*(-9.8* math.sin(alpha*3.14/180))*t**2

print(round(t,2),end=" ")
print(round(OM,2))

#This is an AL physics related problem