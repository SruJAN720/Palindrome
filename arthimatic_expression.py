

## express evaluaton 
## input numbers, 
## operators +,-
## no negative numbers 

testcases = [
    "2 + 3",
    "30 + 11 - 100",
    "231 - 200 - 21 + 11 "
]

def myEval(expr):
    value = 0
    num,op = seperation(expr)
    return value

# def evaluation(num_int_list,opList):
#     while opList:
#         left = num_int_list[-2]
#         right = num_int_list[-1]
#         if opList[-1] == '+':
#             result = left + right
#         elif opList[-1] == '-':
#             result = left - right
#         del num_int_list[-1]
#         del num_int_list[-1]
#         del opList[-1]
#         num_int_list.append(result)
#         print(num_int_list,opList)


def sum(a,b):
    return a+b 

def minus(a,b):
    return a - b 

def map_op(ops,funcs):
    return dict(zip(ops,funcs))

def create_map():
    ops = ['+','-']
    funcs = [ sum,minus]
    return map_op(ops,funcs)
   
def seperation(s):
    pre = 0
    numList = []
    opList = []
    print(s)
    for i in range(len(s)):
        if s[i] in ['+','-']:
            numList.append(s[pre:i])
            opList.append(s[i])
            pre = i +1 
    numList.append(s[pre:len(s)])
    print(numList)
    print(opList)
    num_int_list = list(map(int,numList))
    print(num_int_list)
    opdict = create_map()
    while opList:
        op = opList.pop()
        right = num_int_list.pop()
        left = num_int_list.pop()
        result = opdict[op](left,right)
        
        num_int_list.append(result)
        print(num_int_list,opList)


seperation(testcases[2])




#for test in testcases:
    #print(test, "RESULT " , myEval(test))
