class Item:
    def __init__(self, name, price, quantity=0):
        print(f"An instande created: {name}")
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self, x, y):
        return x * y
    

item1 = Item("Phone", 100, 5)


item2 = Item("Laptop", 1000, 3)
item2.has_numpad = False


print(item1.name)
print(item2.name)
