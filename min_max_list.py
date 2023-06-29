list1 = [1,24,6,34,65,2,6234]
list2 = [90,838,77,23,3,]

def find_min(list1):
    min = 10000000
    for i in list1:
        if i < min:
            min = i
    return min

def find_max(list2):
    max = -1000000
    for j in list2:
        if j>max:
            max = j
    return max

def swap_max_min(list1,list2):
    i = 0
    while i<100:
        i += 1
        maximum = find_min(list1)
        print("Max is ",maximum)
        minimum = find_max(list2)
        print("Min is ",minimum)
        if minimum > maximum:
            list1.remove(maximum)
            list2.remove(minimum)
            list1.append(minimum)
            list2.append(maximum)
            print(list1)
            print(list2)
        else:
            break
    print("list1 is ",list2," list2 is ",list1)


print(find_max(list1))
print(find_min(list1))
swap_max_min(list1,list2)