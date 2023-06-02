#Write a program to iterate the first 10 numbers and in each iteration,
#print the sum of the current and previous number.

print("Printing current and previous number sum in a range (10)")

list = range(10)


for i in range(0,10):
    if i-1 < 0:
        print("Current numer",list[i],"Previous Number", list[i],"sum is", list[i]*2)
    else:
        print("Current Number",list[i], "Previous Number",list[i-1],"sum is", list[i]+list[i-1])
