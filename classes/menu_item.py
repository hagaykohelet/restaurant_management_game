class MenuItem:
    def __init__(self,name:str, price:int, category:str):
        self.name = name
        self.price = price
        self.category = category
        self.available = True

    def get_info(self):
        return f"costumer: {self.name} price: {self.price} is order from {self.category}"

    def set_available(self,status:bool):
        self.available = status


    def is_available(self):
        return self.available




