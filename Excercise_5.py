#Check if First and Last terms of a list is same

numbers_x = [10,20,30,40,10]

numbers_y = [10,15,20,25,30]

#Create a Function
def firstLast_same(numbers_x):
    if numbers_x[0] == numbers_x[-1]:
        print("Result is True")
    else:
        print("Result is False")

#Test Cases
firstLast_same(numbers_x)

firstLast_same(numbers_y)
