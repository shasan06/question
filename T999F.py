'''file= open("result.txt", "r")
s=[]
m=[0,0,0,0]
counter=0
for x in file:
    s.append(x.split())
    counter+=1
s[0].insert(0,"000")
#print(s)
for i in range(1, 4):
    for j in range(1,31):
        if s[i][j]=="x":
            3
        elif s[i][j]==s[0][j]:
            m[i]+=1
        else:
            m[i]-=1
    print(s[i][0]+ " "+ str(m[i]) + " " + " marks")'''


'''def findex(n):
    if a == 0:
        return (0)
    else:
        c, d = 0, 1
        n = 1
        while d <= a:
            if d == a:
                return (n)
                break
            c, d = d, c + d
            n += 1
        else:
            return (-1)


a = int(input())
print(findex(a))'''

numbers = [4,3,2,0,0,0,7]
y = max(numbers)
for y in range(y-1, -1,-1):
    for x in range(len(numbers)):
        if y+1<=numbers[x]:
            print("*", end='')
        else:
            print(" ", end='')
    print()

    #-----------------original

    y = max(numbers)
    #create 2d grid
    grid=[]
    for y in range(y):
        grid.append([])
        for x in range(len(numbers)):
            grid[y].append(0)
    #create
    for y in range(len(grid)-1, -1, -1):
        for x in range(len(grid[y])):
            if y+1<=numbers[x]:
                grid[y][x]=1
            else:
                grid[y][x]=0

    #print
    for y in range(len(grid)-1, -1, -1):
        for x in grid[y]:
            if x == 1:
                print('*', end='')
            else:
                print('',end='')
        print()



