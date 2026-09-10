box_1={"cheetos,suntop,mnm,chocolate,popcorn"}
box_2={"cookies,sandwich,suntop"}
print("box 1:",box_1)
print("box 2:",box_2)

box_1.add("strawberry")
print("box1 with strawberry after")

common_snacks=box_1.intersection (box_2)
print("snacks in both boxes")

import array as arr
box_counts=arr.array('i',[1,9,7,3,2])
print("snack array:", box_counts)

box_counts.append(4)
print("box counts after adding 4")

box_counts.reverse()

print("")
print("HOME COUNTER FOR SNACKS")
print("box 1:", box_1)
print("box 2:", box_2)
print("common snacks:,shared snacks")