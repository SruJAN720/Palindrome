
flow = [10,21,33,45,62,70]

grow = [5,10,42,72,23,65]

def divis_five(flow):
    print("Given List is",flow)
    print("Divisible by five")
    for i in range(len(flow)):
        if flow[i]%5==0:
            print(flow[i])

divis_five(flow)

divis_five(grow)
