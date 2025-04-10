def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If the discount is 20% or higher, it applies the discount;
    otherwise, it returns the original price.
    """
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price  # No discount applied

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Ensure inputs are non-negative
    if original_price < 0 or discount_percent < 0:
        print("Price and discount percentage must be non-negative values.")
    else:
        final_price = calculate_discount(original_price, discount_percent)

        # Display the result
        if final_price == original_price:
            print(f"No discount applied. The final price is: ${original_price:.2f}")
        else:
            print(f"Discount applied! The final price is: ${final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numerical values for price and discount percentage.")
