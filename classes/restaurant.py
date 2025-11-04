from classes.menu import Menu
from classes.order import Order


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = Menu
        self.staff = []
        self.orders = []
        self.money = 1000

    def hire_staff(self,staff_member):
        self.staff.append(staff_member)

    def fire_staff(self,staff_name):
        self.staff.remove(staff_name)

    def create_order(self,customer):
        self.orders.append(Order(customer,0))

