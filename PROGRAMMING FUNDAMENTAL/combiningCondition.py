 #Combining Conditions (E-Commerce Shipping Calculator)

cart_total = 750  # Value in Rupees
is_premium_member = False

if is_premium_member:
    print("Shipping Cost: Free (Premium Perk)")
elif cart_total >= 1000 and not is_premium_member:
    print("Shipping Cost: Free (Orders over ₹1000)")
elif cart_total >= 500 and cart_total < 1000:
    print("Shipping Cost: ₹40 (Standard Delivery)")
else:
    print("Shipping Cost: ₹80 (Low Cart Value Fee)")