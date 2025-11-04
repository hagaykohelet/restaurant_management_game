from classes.staff import Staff

class Chef(Staff):
    def __init__(self,name ,salary,specialty):
        super().__init__(name, salary)
        self.specialty = specialty

    def cook_order(self,order):

        order = "cooking"
        order = "ready"

    def decrease(self):
        super().work()
        self.energy -= 5




