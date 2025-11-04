from classes.customer import Customer
from classes.menu_item import MenuItem
class Order:
    def __init__(self,customer:Customer,order_number):
        self.customer = customer
        self.order_number = order_number
        self.items = []
        self.status = "pending"
        self.total_price = 0


    def add_item(self,menu_item:MenuItem):
        self.items.append(menu_item)
        self.total_price += menu_item.price

    def remove_item(self,menu_item:MenuItem):
        self.items.remove(menu_item)
        self.total_price -= menu_item.price

    def get_total(self):
        return self.total_price

    def set_status(self,new_status):
        self.status = new_status


    def display_order(self):
        for item in self.items:
            print(f"number: {self.order_number}\n{item.get_info()}\ntotal price: {self.total_price}\nstatus of order: {self.status}")



    def is_complete(self):
        return self.status == "delivered"









# c1 = Customer("hagay")
# m1 = MenuItem("asd",123,"drink")
# m2 = MenuItem("asd",123,"drink")
#
# o1 = Order(c1,21)
# o1.add_item(m1)
# o1.add_item(m2)
# o1.set_status("delivered")
# o1.display_order()
