x = 121

z = 12345

def palindrom_check(x):
    y = str(x)[::-1]
    y = int(x)
    if y == x:
        print("It is Pallindrome")
    else:
        print("Number is not a Pallindrome")
        
palindrom_check(x)

palindrom_check(z)
