def common_elements(list1, list2):
    list=[]
    z=-99999
    for x in sorted(list1):
        if x==z: continue
        for y in sorted(list2):
            if x==y:
                list.append(x)
                z=x
                break
    return list



print(common_elements([3, 1, 2], [2, 4, 3]))
print(common_elements([3, 3, 2, -3], [3, 3, 4, 5, -4, -3]))