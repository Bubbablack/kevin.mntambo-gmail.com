
#add multiple numbers
def findSum(str1):
    Sum = 0

    for ch in str1:
        if (ch.isdigit()):
            Sum += int(ch)

    return Sum
 
print(findSum(str1))


#multiply multiple numbers.
def findProd(str2):
    Prod = 1

    for char in str2:
        if (char.isdigit()):
            Prod *= int(char)

    return Prod
 
