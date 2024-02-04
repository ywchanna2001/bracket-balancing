import math

pi = 3.14

a,b = list(map(float,input().split(" ")))
c,d = list(map(float,input().split(" ")))
r = float(input())
theta = float(input())  #by radius


base = math.sqrt((a-c)**2 + (b-d)**2)
a1 = r**2 *( (2*pi-theta)/2 )
a2 = r**2 *(theta/2)
a3 = 0.5 * r* math.cos(theta/2)*base

A1 = a1+a3
A2 = a2-a3
# print("--------------")
# print("a1:"+str(a1))
# print("a2:"+str(a2))
# print("a3:"+str(a3))
# print("A1:"+str(A1))
# print("A2:"+str(A2))
ratio = A2/A1
if(ratio<=1 and ratio>=0):
    print(round(ratio,2))
else:
    print("Can not find a ratio")