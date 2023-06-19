l2 = []
max_size=7

def addElement(l2,element):
    if len(l2)>=max_size:
        print("List at Maximum Capacity")
    else:
        l2.append(element)

def checkIfEmpty(l2):
    if len(l2) == 0:
        return True
    else:
        return False

def printQue(l2):
    print(l2)


def popping(l2):
    if checkIfEmpty:
        return l2.pop()
        
    else:
        print("No Elements")


#### Test Code
def testingCode():
    addElement(l2,10)
    addElement(l2,20)
    printQue(l2)
    popping(l2)
    printQue(l2)
    for i in range(9):
        addElement(l2,i*10)
    printQue(l2)

testingCode()