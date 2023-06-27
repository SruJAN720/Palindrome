x = int(input("Enter a number"))

def return_reversed_number(x):
    number = 0
    while x!= 0:
        y = x%10
        number = number*10 + y
        x = x//10
    return number

print(return_reversed_number(x))
