def number_of_above_averages(n,m,A):
    sum=0
    count=0
    for elem in A:
        for i in elem:
            sum+=i
    average=sum/(n*m)
    for elem in A:
        for j in elem:
            if average<j:
                count+=1
    return count




