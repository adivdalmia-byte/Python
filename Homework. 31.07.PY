s = [5,2,6,8,5,3,6]
print(s)

count=0

for i in s:
    count= count+1

avg=count/len(s)

print("sum=",count)



s.sort()

print("smallest element is:",s[0])

print("largest element is:",s[-1])