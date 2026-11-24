
# Simple Bill Calculator - Week 2 Assignment

# Ask the user to enter the price and quantity
price = float(input("Enter the price of one item: "))
quantity = int(input("Enter the quantity of items: "))

# Calculate the total cost
total = price * quantity

# Display the bill summary using an f-string
print("\n----- BILL SUMMARY -----")
print(f"{quantity} items at {price:.2f} each = {total:.2f}")
print("Thank you for shopping!")

