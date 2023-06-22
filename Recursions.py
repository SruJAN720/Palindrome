
## Recursion reffers to calling upon the same function.
def factorial(n):
    if n <= 1:
       return 1
    else:
        return n*factorial(n-1)
    
fc = factorial(5)
print(5, fc)

def sumOfNaturalNumbers(n):
    if n<=1:
        return 1
    else:
        return n+sumOfNaturalNumbers(n-1)

Nn = sumOfNaturalNumbers(10)

print(Nn)

def towerOfHanoi(n,A,B,C):
    if n == 1:
        print("Move Disk 1 from A to C")
        return
    towerOfHanoi(n-1,A,B,C)
    print("Move disk",n," from source",A," to destination",C)
    towerOfHanoi(n-1,B,C,A)

towerOfHanoi(3,"A","B","C")


l1 = [1,5,300]
l2 = [3,10,250,500]
l3 = []
def merge_sorted_lists(l1,l2):
    l3 = []
    while l1 and l2:
        if l1[0] <= l2[0]:
            l3.append(l1.pop(0))
        else:
            l3.append(l2.pop(0))

    l3 = l3+l1+l2
    print(l3)
    return l3

#big_List = [1,6,-23,654,22,-32,434] 
def merge_sort(big_List):
    print(big_List,len(big_List))
    if len(big_List) <= 1:
        return big_List
    elif len(big_List)%2 == 0:
        k = int(len(big_List)/2)
    else:
        k = int((len(big_List)+1)/2)
    s1 = merge_sort(big_List[0:k])
    print(s1)
    s2 = merge_sort(big_List[k:])
    print(s2)
    return merge_sorted_lists(s1,s2)

ms = merge_sort([1,6,-23,654,22,-32,434] )
print(ms)
