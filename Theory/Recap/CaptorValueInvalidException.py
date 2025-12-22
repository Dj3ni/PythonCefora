class CaptorValueInvalidException(Exception):
    def __init__(self, msg = "Invalid value"):
        super().__init__(self, msg)

