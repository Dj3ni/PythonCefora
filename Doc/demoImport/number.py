class Number:
    def __init__(self, value):
        self.value = value

    # +
    def __add__(self, other):
        return self.value + other
    
    # -
    def __sub__(self, other):
        return self.value - other
    
    # *
    def __mul__(self, other):
        return self.value * other
    
    # / (division compléte)
    def __truediv__(self, other):
        return self.value / other
    
    # // (division entière)
    def __floordiv__(self, other):
        return self.value // other

number = Number(5)
print(number + 5)
print(number - 5)
print(number / 4)
print(number // 4)