ss = str(input("Please Enter A String:"))

print("Original String is", ss)

print("Printing only even index characters")

def even_indexCharacters(ss):
    for i in range(len(ss)):
        if i % 2==0:
            print(string[i])
        else:
            print("")

even_indexCharacters(ss)
