products_list = [29.25, 48.99, 99.98, 124.65, 214.30, 543.90, 799.85]
discount_percent = 60
discounts_list = []
value_with_discount_list = []
print("**Discount table:**")
for product_price in products_list:
    amount_of_discount = product_price * discount_percent / 100
    discounts_list.append(amount_of_discount)
    price_discount = product_price - amount_of_discount
    value_with_discount_list.append(price_discount)
    print('**', product_price, round(price_discount, 2), round(amount_of_discount, 2), '**')
