import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price}, is not greater than zero."
        assert quantity >= 0, f"Quantity {quantity}, is not greater than zero."

        # Assign to self object
        print(f"An instande created: {name}")
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
            with open('app1/data.csv', 'r') as f:
                 reader = csv.DictReader(f)
                 items = list(reader)

            for item in items:
                Item(
                     name=item.get('name'),
                     price=float(item.get('price')),
                     quantity=int(item.get('quantity')),
                )    
    @staticmethod
    def is_integer(num):
         # We will count out the floats that are point zero
         # For i.e: 5.0, 10.0
         if isinstance(num, float):
              # Count out the floats that are point zero
              return num.is_integer()
         elif isinstance(num, int):
              return True
         else:
              return False
         

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
    
class Phone(Item):
     def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes
        super().__init__(
             name, price, quantity
        )

        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal "

        # Assign to self object
        print(f"An instande created: {name}")
        self.broken_phones = broken_phones

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



