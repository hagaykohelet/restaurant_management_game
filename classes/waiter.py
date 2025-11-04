from classes.staff import Staff
from classes.menu import Menu
from classes.customer import Customer
from classes.order import Order

class Waiter(Staff):
    def __init__(self,name,salary):
        super().__init__(name,salary)
        self.tips = 0

    def take_order(self,customer:Customer,menu:Menu):
        new_order = Order(customer,0)
        while True:
            menu.display_menu()
            choice = input("please choice something from menu or Q for exit")
            for item in menu.items:
                if choice == item.name:
                    new_order.add_item(choice)
                if choice == "Q":
                    break
            return new_order

    def serve_order(self,order:Order):
        order.set_status("delivery")
        if order.customer.is_happy():
            print("high satisfaction")
        else:
            print("low satisfaction")

    def receive_tip(self,amount):
        self.tips += amount

    def get_total_earnings(self):
        return self.salary + self.tips


