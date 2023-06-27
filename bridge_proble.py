# There are four people on the left side of a bridge. Only two people can
# cross the bridge at a time. And one person can return from the right side
# of the bridge. Generate all the combinations and the time taken for each

#For more complicated cases, use an object to store data
""" class Person:
    def __init__(self,name,time):
        self.name = name
        self.time = time
    def get_time(self):
        return self.time """

#Define some Parameters
left_side = [1,2,5,10]
right_side = []
time = 0

#Create a function to understand the current side
def current_stituation():
    print("On the left side ",left_side)
    print("On the right side ",right_side)
#When crossing, only two people may cross the bridge at a time
def crossing(c1,c2):
    global time
    if len(left_side) == 0:
        print(" CALLED when left_Side empty ")
        return 
    print(" LEFT SIDE CROSSING ",left_side,c1,c2 ,right_side," TIME ",time)
    if left_side[c1] == left_side[c2]:
        return print("Invalid Input")
    elif c1>c2:
        time = time + left_side[c1]
        right_side.append(left_side.pop(c1))
        right_side.append(left_side.pop(c2))
    elif c1<c2:
        time = time + left_side[c2]
        right_side.append(left_side.pop(c2))
        right_side.append(left_side.pop(c1))
    if len(left_side) == 0:
        return 
    #current_stituation()

#When returning, only one person can come back
def returning(r1):
    global time
    print(" LEFT SIDE RETURNING ", left_side, r1,right_side, " TIME ",time)
    if len(left_side) == 0: #Problem is solved
        print(" CALLED when left_Side empty ")
        return 
    else:
        time = time + right_side[r1]
        left_side.append(right_side[r1])
        right_side.pop(r1)
    #current_stituation()

def solution():
    print("LEFT ", left_side, "RITHT ",right_side)
    while left_side:
        crossing(0,1)
        #print("Next move")
        returning(1)
        #print("Next move")
    print("total time ",time)
solution()
    
                

