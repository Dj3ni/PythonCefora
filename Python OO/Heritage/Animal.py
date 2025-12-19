class Animal:
    def __init__(self, paws):
        self._paws = paws

    @property
    def paws(self):
        return self._paws

    @paws.setter
    def paws(self, paws):
        self._paws = paws

    def __str__(self):
        return "Animal: "

    def cry(self):
        pass
    def move(self):
        pass

class Dog(Animal):
    def __init__(self):
        super().__init__(4)

    def cry(self):
        """
            Method allowing Dog to bark
            :param self: instance
        """
        print("Wouf!")

    def move(self):
        print("Runs")

    # return when instance is printed
    def __str__(self):
        return super().__str__() + "It's a dog!"

class Cat(Animal):
    def __init__(self):
        super().__init__(4)

    def cry(self):
        print("Miaou!")

    def move(self):
        print("Walks")

class Fish(Animal):
    def __init__(self):
        super().__init__(0)

    def cry(self):
        print("Bloup!")

    def move(self):
        print("Swims")

class Snake(Animal):
    def __init__(self):
        super().__init__(0)

    def cry(self):
        print("Sssss")

    def move(self):
        print("Crawls")

zazou = Dog()
print(zazou.move())
print(zazou.cry())
print(isinstance(zazou, Dog))
print(isinstance(zazou, Cat))
print(zazou)
print(zazou.cry.__doc__)