s = "2+3+10-4"

s1 = "(-2) + 3 + 4 - 20"
z = "312-433+51-611"

def conversion(sl):
    return int(sl)


def tokenisation(s):
   """  numStack = []
    ppos = -1
    res = 0
    opStack = []
    for pos in range(len(s)):
        if s[pos] in ['+','-']:
            #opStack.append(s[pos])
            numStack.append(conversion(s[ppos+1:pos]))
            opStack.append(s[pos])
            ppos = pos 
    numStack.append(conversion(s[ppos+1:len(s)]))
    print(numStack)
    print(opStack)
    while opStack:
        left = numStack[-2]
        right = numStack[-1]
        op = opStack[-1]
        print( left, op, right)
        opStack.pop()
        if op == '+':
            res = left + right 
        else:
            res = left - right 
        numStack.pop()
        numStack.pop()
        numStack.append(res)
        print(numStack)
        print(opStack)
    print(res) """

tokenisation(s)  
tokenisation(z)