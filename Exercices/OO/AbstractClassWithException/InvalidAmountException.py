
class InvalidAmountException(Exception):

    def __init__(self, msg = "Invalid amount"):
        super().__init__(msg)

