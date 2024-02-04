tot = int(input())
cars = 0
three_wheels = 0
bikes = 0

if(tot%4 == 0):
    cars = tot/4
else:
    if(tot%4 == 3):
        cars = tot//4
        three_wheels = 1
    elif(tot%4 == 2):
        cars = tot//4 -1
        three_wheels = 2
    else:
        cars = tot//4-1
        three_wheels =1
        bikes =1

print(cars,end=" ")
print(three_wheels,end=" ")
print(bikes)
