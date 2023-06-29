def square_digits(n):
    nstr = str(n)
    newn = 0
    for i in nstr:
        newn = int(i)*int(i) + newn
    return newn

print(square_digits(10))

def check_isHappy(n):
    r = 0
    while n>9 and r<10:
        r = r+1
        newn = square_digits(n)
        if newn ==1:
            return True
        n = newn
    return False

print(check_isHappy(13))

def find_next_happy(n):
    result = -1
    for x in range(100):
        if check_isHappy(n+x+1) == True:
            result = n+x+1
            break
    return result

def test_happy():
    for x in [8,10,13]:
        print(x,find_next_happy(x))

test_happy()
