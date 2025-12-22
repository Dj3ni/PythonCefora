from datetime import datetime
from Subscription import Subscription

class User:
    def __init__(self, customer_number:str,firstname:str, lastname:str, email:str, subscription: Subscription):
        self._customer_number = customer_number
        self._firstname = firstname
        self._lastname = lastname
        self._email = email
        self._historical_subscriptions_billing = []
        self.subscription = self.subscribe(subscription)
        self._billing_amount = self.billing_amount()

    @property
    def customer_number(self) -> str:
        return self._customer_number
    @customer_number.setter
    def customer_number(self,customer_number:str) ->None:
        self._customer_number = customer_number

    @property
    def firstname(self) -> str:
        return self._firstname
    @firstname.setter
    def firstname(self,firstname:str) -> None:
        self._firstname = firstname

    @property
    def lastname(self)-> str:
        return self._lastname
    @lastname.setter
    def lastname(self,lastname:str) -> None:
        self._lastname = lastname

    def fullname(self) -> str:
        return f'{self.firstname} {self.lastname}'

    @property
    def email(self) -> str:
        return self._email
    @email.setter
    def email(self,email:str) -> None:
        self._email = email

    @property
    def historical_subscriptions_billing(self) -> list:
        return self._historical_subscriptions_billing

    def subscribe(self, subscription_type:Subscription) -> Subscription:
        self._historical_subscriptions_billing.append({
            "current_subscription": subscription_type.name,
            "price": subscription_type.price,
            "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })
        return subscription_type

    def change_subscription(self,new_subscription:Subscription)-> None:
        if new_subscription == self.subscription:
            raise Exception("You already have that subscription!")

        self._historical_subscriptions_billing.append({
            "old_subscription": self.subscription.name,
            "current_subscription": new_subscription.name,
            "price": new_subscription.price,
            "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        })
        self.subscription = new_subscription
        self._billing_amount += new_subscription.price

    def billing_amount(self) -> float:
        if 1 <= datetime.now().day <= 31:
            return self.subscription.price
        else:
            raise Exception("Invalid day")