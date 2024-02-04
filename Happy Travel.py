t = int(input())

while t:
    moves = 0
    n,k = list(map(int,input().split(" ")))
    c = []
    w = []

    for i in range(0,n):
        c[i],w[i] = list(map(int,input().split(" ")))
    
    t-=1

    #This is 1st comment.