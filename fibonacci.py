'''prev=0
curr=1
i=3
print(prev,end=" ")
print(curr,end=" ")
while(i<=20):
    next= prev+curr
    print(next, end=" ")
    prev=curr
    curr=next
    i+=1'''


# first = 2000

'''prev=0
curr=1
print(prev, curr, end=" ")
count=2
next = prev+curr


while(next<2000):
    print(next, end=" ")
    count += 1
    prev = curr
    curr = next
    next = prev + curr



print(count)'''

'''def search(str, lst,size):
    for x in range(0, size):
        if str==lst[x]:
            return x

    return -1

str="a,b"
lst=["a","b","c"]
lst2=["a","b","c", "a,b"]
print(search(str, lst, 3))
print(search(str, lst2, 4))'''

# Guessing game
'''import random
rand=random.randint(0,100)
user_guess=int(input())
count=1
while(user_guess!=rand):
    if user_guess<rand:
        print("To Low . Guess again:")
    else:
        print("To High . Guess again")
    user_guess = int(input())
    count+=1

print("correct. It took you "+ str(count) + " guesses")'''









