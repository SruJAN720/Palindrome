
x = int(input("Please Enter The Amount "))

def income_tax(x):
    #First 10,000 is free
    if x<=10000:
        print("The Tax Amount is zero")
    #Next 10,000 is 10% tax
    elif x>10000 and x<=20000:
        print("The Tax Amount is ",(x-10000)/10)
    #Remaining amount is 20% tax
    elif x>20000:
        print("The Tax Amount is ",1000+(x-20000)/5 )

income_tax(x)
