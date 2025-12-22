def regular_price():
    return 3.5

def happy_hour_price():
    return 2

class Bar:
    def __init__(self, strategy):
        self.strategy = strategy

    def sell_a_beer(self):
        return self.strategy()
    
bar = Bar(regular_price)
print(bar.sell_a_beer())