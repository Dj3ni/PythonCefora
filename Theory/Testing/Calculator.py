
class Calculator:

    def addition(self,a,b):
        return a+b

    def division(self,a,b):
        if b == 0:
            raise ZeroDivisionError
        else:
            return a/b
        return a/b