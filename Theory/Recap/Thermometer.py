from Captor import Captor
from Theory.Recap.CaptorValueInvalidException import CaptorValueInvalidException


class Thermometer(Captor):
    unit = "°C"
    def __init__(self, value = 0):
        super().__init__(value)

    def __str__(self):
        return f"{self.value}{self.unit}"

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if -273 <= value <= 70:
            self._value = value
        else:
            raise CaptorValueInvalidException("The value must be between -273 and 70 °C")


try:
    thermometer = Thermometer(70)
    # print(str(thermometer.value) + thermometer.unit)
    print(thermometer)
except CaptorValueInvalidException as e:
    print(e)
except:
    print("Unexpected error encountered.")

