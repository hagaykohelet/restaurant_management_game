from classes.waiter import Waiter
from classes.customer import Customer
from classes.staff import Staff
from classes.order import Order
from classes.menu_item import MenuItem
from classes.chef import Chef
from classes.restaurant import Restaurant
from classes.menu import Menu

if __name__ == "__main__":
    menuitem1 = MenuItem("pizza",50,"dairy")
    menuitem2 = MenuItem("meet",70,"meet")
    menuitem2.set_available(False)
    menu = Menu()
    menu.add_items(menuitem1)
    menu.add_items(menuitem2)
    menu.display_menu()

    customer = Customer("hagay")

