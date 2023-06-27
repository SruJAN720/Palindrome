import itertools
stuff = [1,2,5,10]
sub_set = itertools.combinations(stuff,4)

def cost_of_travel(pl):
    if not pl:
        return 0 
    cost = max(pl)
    return cost 

def pick_two (plist):
    if len(plist) <= 1:
        return [],plist
    sublist = []
    sublist.append(plist.pop(0))
    sublist.append(plist.pop(0))
    return sublist,plist 

def pick_one (plist):
    if len(plist) == 0:
        return [],plist 
    sublist = []
    sublist.append(plist.pop(0))
    return sublist, plist 

def solution(plist):
    left_list = list(plist) 
    right_list = []
    travel_cost = 0
    iter = 0
    travel_path = [ ]
    while len(left_list)!= 0:
        print(" LEFT ",left_list,  " RIGHT SIDE ",right_list, " TRAVEL ", travel_cost )
        subf,left_list = pick_two(left_list)
        travel_cost += cost_of_travel(subf)
        right_list += subf 
        travel_path += [ "LEFT {} , RIGHT {} , cost {}".format(left_list,right_list,travel_cost) ]
        if len(left_list) == 0:
            break  
        
        subr, right_list = pick_one(right_list)
        travel_cost += cost_of_travel(subr)
        left_list += subr 
        travel_path += [ "LEFT {} , RIGHT {} , cost {} ".format(left_list,right_list,travel_cost) ]

    print(" Total cost ", travel_cost)
    return travel_cost ,travel_path
def gen_combinations(nlist):
    combi = []
    if len(nlist) <= 1:
        return [nlist] 
    else:
        print(" LIST SIZE ", len(nlist))
        for pos in range(len(nlist)):
            print(" POS ",pos, nlist[pos])
            nlistminus = nlist[0:pos] + nlist[pos+1:]
            sublists = gen_combinations(nlistminus)
            print(sublists)
            for sublist in sublists:
                ssl = [nlist[pos]] + sublist
                combi.append(ssl)
                #print(combi)
        return combi 

import sys 

nlist = [1,2,5,10]
nx = gen_combinations(nlist)
tcmin = 10000 
tpath = []
bestpos = []
for cx in nx:
    print(cx)
    tc,tp = solution(cx)
    print(cx, " cost ", tc, tp  )
    if tc < tcmin:
        tcmin = tc  
        tpath = tp 
        bestpos = cx 
print(" BEST ")
print( cx, " TP ", "\n".join(tpath), " cost ", tcmin )
print(len(nx))
