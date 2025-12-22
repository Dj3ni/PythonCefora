from abc import ABC, abstractmethod
from CaptorValueInvalidException import CaptorValueInvalidException

# Inherit from Abstract Base Class
class Captor(ABC):
    # attribute
    unit = None

    # constructor
    def __init__(self, value):
        self.value = value

    # getter
    @property
    def value(self):
        return self._value

    # setter
    @value.setter
    def value(self, value):
        if value < 0:
            # exception
            raise CaptorValueInvalidException("The value cannot be negative")
        self._value = value

    @abstractmethod
    def __str__(self):
        pass


# Execution
if __name__ == "__main__":
    try:
        captor = Captor(5)
        print(captor.value)
    except CaptorValueInvalidException as e:
        print(e)
    except:
        print("Unexpected error encountered.")