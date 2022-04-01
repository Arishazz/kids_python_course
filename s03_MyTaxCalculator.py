# i had notes to help me but i deleted them by accident
tax_rate = 0.13
price = eval(input("What is the price of your item?"))
quantity = eval(input("How many of this item would you like to purchase?"))
subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax
print("The cost of your item(s) including tax is $", total, ".")


  
