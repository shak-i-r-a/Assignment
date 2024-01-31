Item = input("Enter Item: ")
Item_price = input("What's The price Of the item: ")
Quantity = input("What's the quantity of the item: ")
Feedback = input("Give your experience while shopping: ")

Total_Amount = int(Item_price)* int(Quantity)
Discount = int(Total_Amount)* float(0.1)
Final_Amount = int(Total_Amount) - float(Discount)

print(f"Total Amount is {Total_Amount}")
print(f"Discount is {Discount}")
print(f"Final Amount is {Final_Amount}")
