list1 = [1,2,4,6,8,13,17]
list2 = [2,7,8,13,16,17]

def union_function(list1,list2):
    #Step 1: Determine Mutual Elements
    mutual_elements = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i]==list2[j]:
                mutual_elements.append(list2[j])
     #Step 2: Remove similar elements           
    for k in range(len(mutual_elements)):
        list2.remove(mutual_elements[k])
    
    union_list = list1 + list2
    
    return union_list

print(union_function(list1,list2))


    
    
    
    