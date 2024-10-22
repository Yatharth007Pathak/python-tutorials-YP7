'''
If cost price and sellig price of an item is input through the keyboard, 
write a program to determine whether the seller has made profit or incurred loss or no profit or loss. 
Also determine how much profit he made or loss he incurred
'''

cost_price = int(input("Enter the cost price:"))
selling_price = int(input("Enter the selling price:"))

if selling_price > cost_price:
    print("PROFIT of", selling_price - cost_price)

elif selling_price < cost_price:
    print("LOSS of", cost_price - selling_price)

else:
    print("Neither Profit nor Loss")