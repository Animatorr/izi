class Car():
    def __init__(self,name):
        self.name=name
    def fullname(self):
        print(self.name)
class Electro_car(Car):
    def fullname(self):
        print("Ti gey")
    def __init__(self,name):
        super().__init__(name)

mytesla=Electro_car("Model X")
mytesla.fullname()