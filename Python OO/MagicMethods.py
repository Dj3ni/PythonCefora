class MagicMethods:
    def __init__(self):
        self.value = 5

    # +, - , /, // , *, %, **
    def __add__(self, other):
        return self.value + other
    def __iadd__(self, other):
        self.value += other

    def __sub__(self, other):
        return self.value - other
    def __isub__(self, other):
        self.value -= other

    def __mul__(self, other):
        return self.value * other
    def __imul__(self, other):
        self.value *= other

    def __truediv__(self, other):
        return self.value / other
    def __rtruediv__(self, other):
        self.value /= other

    def __floordiv__(self, other):
        return self.value // other
    def __rfloordiv__(self, other):
        self.value //= other

    def __pow__(self, other):
        return self.value ** other
    def __rpow__(self, other):
        self.value **= other

    # modulos
    def __mod__(self, other):
        return self.value % other
    def __rmod__(self, other):
        return self.value % other
    def __rdivmod__(self, other):
        return divmod(self.value, other)

    def __abs__(self):
        return self.value
    def __floor__(self):
        return self.value
    def __ceil__(self):
        return self.value

    # Comparisons
    def __lt__(self, other):
        return self.value < other
    def __gt__(self, other):
        return self.value > other
    def __ge__(self, other):
        return self.value >= other
    def __le__(self, other):
        return self.value <= other
    def __eq__(self, other):
        return self.value == other
    def __ne__(self, other):
        return self.value != other

    # Collections
    def __getitem__(self, item):
        return self.value
    def __setitem__(self, key, value):
        self.value = value
    def __iter__(self):
        return iter(self.value)
    def __reversed__(self):
        return reversed(self.value)



