print("Tip Calculator")

value = int(input("Enter the cost of the bill:  >"))

tip = input("Do you want to charge any tip? > Y/n").lower()

if tip == "y":
    tip_value = int(input("Enter the percentage of the tip: >  "))
    tip_value = tip_value / 100
    total = value + (value * tip_value)
    print("The total bill is {}".format(total))
else:
    print("The total bill is:  {}".format(value))    
