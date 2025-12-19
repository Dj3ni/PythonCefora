class InvalidCalculatorException(Exception):
    pass

value = int("0")

try:
    print(value/0)
    raise InvalidCalculatorException('Invalid calculation')
except ValueError:
    print('Value not a number')
except ZeroDivisionError:
    print('Division by zero impossible')
except Exception as e:
    print("Oops, something went wrong...", e)
else:
    print("Yay, it worked!")
finally:
    print('End of my try..except')

while True:
    try:
        value = int(input("Enter a positive number: "))
        if value <= 0:
            raise Exception('Value not a positive number')
    except Exception as e:
        print(e)
    else:
        print(f"Yay, it worked! Your number was: {value}")
        break
