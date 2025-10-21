def calculate(result, operator, next_number):
    match operator:
        case "+":
            result += next_number
        case "-":
            result -= next_number
        case "*":
            result *= next_number
        case "/":
            result /= next_number
        case "%":
            result %= next_number
        case "//":
            result //= next_number
        case "**":
            result **= next_number
    return result



print("Welcome to Calculator")
number_a = float(input("Enter the first number: "))
result = number_a
userInput = ""

while (userInput != "="):
    operator = input("Enter the operator: ")
    userInput = operator
    if(operator != '='):
        number_b = float(input("Enter the next number: "))
        result = calculate(result, operator, number_b)


print("The result is:", result)

