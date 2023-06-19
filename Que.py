l1 = []
max_size = 9


def addElement(l1,element,max_size):
    # edge case 9
    if len(l1) >= max_size:
        return False 
    l1.append(element)
    return True

def popping(l1):
    if checkIfEmpty(l1):
        print("Not Possible")
        return None 
    ## return zero element
    return l1.pop(0)
    
def checkIfEmpty(l1):
    if len(l1) == 0:
        return True
    else:
        return False

def printQue(l1):
    print(l1)



#test code 
def test_code():
    printQue(l1)
    addElement(l1,10,max_size)
    addElement(l1,15,max_size)
    if checkIfEmpty(l1):
        print("Code is wrong ")
    else:
        print("Code is good")
    printQue(l1)
    ele = popping(l1)
    if ele == 10:
        print(ele, " good")
    else:
        print(" bad code ",ele)
    print(popping(l1))
    ele = popping(l1)
    if ele:
        print("Some strange element")
    else:
        print(" srujan is great ")
    
    for i in range(9):
        addElement(l1,i*200,max_size)
    if not addElement(l1,201,max_size):
        print("Code is good")
    else:
        print(" MAX is not good")
    printQue(l1)

### main 
test_code()