items=["harry potter","percy jackson","alex rider"]
copy_counts=[7,6,5]

inventory={items: for items in items in zip(items,copy_counts)}
print("full inventory",inventory)

in_copy_items=(items for items in items if inventory(items)>5)
print("items in copy",in_copy_items)

chosen_item=input("what item would you like to buy")
if chosen_item is not in inventory or inventory[chosen_item==0]
    exit()

prices=[20,40,15]
markup=input("enter marked up price")

marked_up_prices=list(map(lambda p:p+markup price))
print("marked_up_prices", marked_up_prices)

item_index=item.index(chosen_item)
chosen_prices=marked_up_prices[item_index]
print("price of",chosen_prices."after markup",chosen prices)

inventory[chosen_item]=inventory[chosen_item-1]

print("=========BOOK STORE======")

    



