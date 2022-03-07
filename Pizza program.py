number_pizzas = eval(input("How many pizzas to you want? "))
cost_per_pizza = eval(input("How much does each pizza cost? "))
subtotal = number_pizzas * cost_per_pizza
tax = 0.08
sales_tax = subtotal * tax
total = subtotal + sales_tax
print("The total cost is $", total)
print("This includes $", subtotal, "for the pizza amd $", sales_tax, "in sales tax")
