class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

class Car(Vehicle):
    def __init__(self):
        # Go through parent constructor
        super().__init__(4)

    def ride(self):
        print("I'm driving my car!")

class Boat(Vehicle):
    def __init__(self, wheels):
        super().__init__(0)

    def sail(self):
        print("I'm sailing my boat!")

# Classic Heritage
class Mercedes(Car):
    def __init__(self, power):
        # Go through parent constructor
        super().__init__()
        self.power = power

# Multiple Heritage
class Citroen(Car, Vehicle):
    def __init__(self, power):
        Car.__init__(self)
        Vehicle.__init__(self,4)
        self.power = power

class CrocoBus(Car, Boat):
    def __init__(self):
        Boat.__init__(self,0)
        Car.__init__(self)