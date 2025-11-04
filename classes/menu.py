from classes.menu_item import MenuItem
class Menu:
    def __init__(self):
        self.items = []

    def add_items(self,menu_item:MenuItem):
        self.items.append(menu_item)

    def remove_item(self,item_menu:MenuItem):
        self.items.remove(item_menu)

    def get_item_by_name(self,name):
        for item in self.items:
            if item.name == name:
                return item.name
        return f"{name} not found"

    def get_item_by_category(self,category):
        items_category = []
        for item in self.items:
            if item.category == category:
                items_category.append(item.name)
        return items_category

    def display_menu(self):
        for item in self.items:
            if item.available:
                print(f"item: {item.name} category: {item.category}")

    def get_total_items(self):
        count_items = 0
        for item in self.items:
            count_items += 1
        return count_items



