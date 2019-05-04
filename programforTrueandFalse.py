


file = open("results.txt", "r")

s=[] # list of list
m=[0,0,0,0] # marks for each student

for x in file:
    s.append(x.split())
#for i in range(4):
    #print(s[i])
for i in range(1,4):
    for j in range(1,31):
        if s[i][j]==s[0][j]:# standat list is compared with a student answer
            m[i]+=1

for i in range(1,4):
    print(s[i][0]+ " " +str(m[i])+ " marks")
