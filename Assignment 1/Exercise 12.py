# Develop a program that calculates the total price of a discounted
# item. Get the original price of the item and calculate the sales
# price with a 15% discount. The tax rate is 10%. Display the original
# price, sales price, and the total price with the tax.

originalPrice = float(input("Enter the item's original price: $"))
discount = 0.15
taxRate = 0.10

discountedAmount = originalPrice * discount
discountedPrice = originalPrice - discountedAmount

taxPrice = (discountedPrice * taxRate) + discountedPrice

print(f"Original Price: $", '{:2,.2f}'.format(originalPrice))
print(f"Discounted Amount: $", '{:2,.2f}'.format(discountedAmount))
print(f"The total amount due: $", '{:2,.2f}'.format(taxPrice))