city = input("What city do you want to visit: ")
state = input("What state is that city in: ")
print("Your destination of choice is " + city + ", " + state)

total_cost = input("What is the total cost of your item?: ")
discount = input ("What is the discount percentage: ")
final_cost = (float(total_cost) -(float(total_cost)*(float(discount)*.01)))
print("The discount on a item costing $" + str(total_cost) + " with a discount of " + str(discount) + "% makes the total $" + str(final_cost))
