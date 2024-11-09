from item import Item
from phone import Phone


Item.instantiate_from_csv()

print(Item.all)


















# item1 = Item("Phone", 100, 5)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)
# # item2.has_numpad = False

# print(Item.all)



# print(item1.calculate_total_price())
# print(item2.calculate_total_price())
# print(Item.__dict__) # All the attributes for Class level
# print(item1.__dict__) # All the attributes for instance level
# item2.pay_rate = 0.7
# print(item1.price)
# print(item2.price)

#USING CSV
#Item.instantiate_from_csv()

#INHERITANCE
# phone1 = Phone("bkPhonev10", 500, 5, 1)
# print(phone1)


