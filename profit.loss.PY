actual_cost=float(input("Please enter the actual product price:"))
sales_amount = float(input("please enter the sales amount"))

if (sales_amount > actual_cost):
  amount=sales_amount - actual_cost
  print(amount)
else:
  print("No profit!!!")