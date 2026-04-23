n=int(input("enter your digit"))
numLen = 0
while n > 0 :
    numLen = numLen +1
    n = int(n//10)
    print("the number of digits in the given number:" , numLen)
          
