'''def shortest_continuous_segments(s):


    list1=[]
    z=-1
    for i in range(len(s)):
        if s[i]==z:
            continue
        count=1
        if i < len(s)-1:
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    count+=1;
                else:
                    list1.append((s[i],count))
                    z=s[i]
                    break
    print(list1)



    d=dict()
    for elements in s:
        if elements in d.keys():
            d+=1

    return d




print(shortest_continuous_segments([1, 1, 2, 2, 2, 1, 1, 1]))'''


def shortest_continuous_segments(s):
    list1 = []
    list2 = []
    z = -99999999

    for i in range(len(s)):
        if s[i] == z:
            continue
        else:
            z = s[i]
            count = 1
            for j in range(i + 1, len(s)):
                if s[j] == z:
                    count += 1
                else:
                    list1.append((z, count))
                    break
    list1.append((z, count))

    print(list1)

    s = 99999
    for e in list1:
        if e[1] < s:
            s = e[1]

    for e in list1:
        if e[1] == s:
            list2.append(e)

    max = -9999 # multiple tuple
    for e in list2:
        if e[0] > max:
            max = e[0]

    for e in list2:
        if e[0] == max:
            ret = e

    return ret



print(shortest_continuous_segments([1, 1, 2, 2, 2, 1, 1, 1]))
print(shortest_continuous_segments([1, 1, 2, 2, 2, 1, 1, 1, 5,5,8,8]))