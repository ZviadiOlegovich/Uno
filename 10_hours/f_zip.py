product = ['toy', 'banana', 'car', 'HDD']

price = [45.99, 70.98, 50, 20.30, 56.78]


product_price_zip = zip(product, price)

print(product_price_zip)
print(type(product_price_zip))

product_price_zip = dict(product_price_zip)

print(product_price_zip)
print(type(product_price_zip))
