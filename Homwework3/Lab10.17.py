class ItemToPurchase:
    def __init__(self):
        self.item_name = "None"
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        print(self.item_name, self.item_quantity, "@ ${:.0f}".format(self.item_price), "= ${:.0f}".format(self.item_price * self.item_quantity))


item1 = ItemToPurchase()
print("Item 1")
item1.item_name = input("Enter the item name:\n")
item1.item_price = float(input("Enter the item price:\n"))
item1.item_quantity = int(input("Enter the item quantity:\n"))

print()

item2 = ItemToPurchase()
print("Item 2")
item2.item_name = input("Enter the item name:\n")
item2.item_price = int(input("Enter the item price:\n"))
item2.item_quantity = int(input("Enter the item quantity:\n"))

print()

print("TOTAL COST")
item1.print_item_cost()
item2.print_item_cost()
print()
print("Total: ${:.0f}".format((item1.item_quantity * item1.item_price) + (item2.item_quantity * item2.item_price)))
