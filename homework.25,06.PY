def calculate(v,s):
     return(v-s)
    

s =float(input("enter the bill amount:" ))
v =float(input("enter the amount payed:"))


if v >= s:
     print(calculate(v,s))

else:
     print("not possible")
    
