def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)  # Calculate the discount amount
        final_price = price - discount_amount  # Subtract discount from the original price
        return final_price
    else:
        return price  # Return original price if discount is less than 20%

# Prompt the user to enter the original price and discount percentage
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the function
final_price = calculate_discount(price, discount_percent)

# Print the final price or the original price if no discount was applied
print(f"The final price is: {final_price}")
