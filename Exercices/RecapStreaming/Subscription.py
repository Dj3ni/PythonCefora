from datetime import datetime

class Subscription:
    def __init__(self,name:str, price:float, devices:int, quality:list):
        self._name = name
        self._price = price
        self.devices = devices
        self.quality = quality
        self._price_history = []

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name:str):
        self._name = name

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,new_price:float):
        if new_price < 0:
            raise ValueError("Price cannot be less than O")
        self._price = new_price
        self._price_history.append({
            "old_price":self._price,
            "new_price":new_price,
            "date_change": datetime.now()
        })
    @property
    def get_price_history(self):
        return self._price_history

class BasicSubscription(Subscription):
    def __init__(self):
        super().__init__("Basic", 5.00,1, ["SD"])

class StandardSubscription(Subscription):
    def __init__(self):
        super().__init__("Standard", 10,2, ["SD","HD"])

class PremiumSubscription(Subscription):
    def __init__(self):
        super().__init__("Premium",15,4,["SD", "HD","UHD"])