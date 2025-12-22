from Calculator import Calculator
import pytest

class TestCalculator:

    calc = Calculator()

    def test_addition(self):
      assert self.calc.addition(2, 3) == 5

    @pytest.mark.parametrize("a,b,result", [
        (1, 2, 3),
        (-1, 1, 0)
    ])
    def test_multiple_addition(self, a, b, result):
        assert self.calc.addition(a, b) == result

    def test_division_by_zero(self):
        # If this error is sent, the test is passed
        with pytest.raises(ZeroDivisionError):
            self.calc.division(2,0)
            self.calc.division(10,0)