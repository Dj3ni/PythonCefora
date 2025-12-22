def my_decorator(function):
    # *args => paramètre positionné
    # **kwargs => paramètre nommé
    def wrapper(*args, **kwargs):
        print("Avant la fonction")
        function(*args, **kwargs)
        print("Après la fonction")
    return wrapper


@my_decorator
def work(name):
    print("Ma méthode marche")

work(name = "Henry")

def repeat_decorator(n):
    def decorator(function):
        def wrapper(*args, **kwargs):
            for i in range(n):
                function(*args, **kwargs)

        return wrapper
    return decorator

@repeat_decorator(3)
def test():
    print("Je teste ma méthode")

test()
        