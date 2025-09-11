class Phone:
    category = 'Electronics'

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

phone1 = Phone("Apple", 15000)
phone2 = Phone("Samsung", 14000)

print(phone1.category)
print(phone1.price)

phone1.price = 12000
print(phone1.price)

Phone.category = 'Gadgets'
print(phone1.category)
print(phone2.category)