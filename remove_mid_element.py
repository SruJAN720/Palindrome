stack1 = [10,20,30,40,50]
stack2 = [10,20,30,40]
stack10= int[100]
stack3 = [10,20,30,40,50]
def remove_mid_element(stack):
    x = int(len(stack))
    if x%2 == 0:
        mid = x // 2 - 1
    else:
        mid = x // 2 
    print("MID ",mid)
    for pos in range(mid,len(stack)-1):
        stack[mid] = stack[mid+1]
        print(pos)
    stack[-1] = None 
    return stack

print(remove_mid_element(stack3))
