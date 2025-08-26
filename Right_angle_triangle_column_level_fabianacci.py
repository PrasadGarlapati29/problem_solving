a,b=0,1
n=4

triangle=[[] for i in range(n)]

for col in range(n):
    for row in range(col,n):
        triangle[row].append(a)
        a,b=b,a+b

for row in triangle:
    for i in row:
        print(i,end=" ")
    print()
