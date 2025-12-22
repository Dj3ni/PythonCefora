from Exercices.RecapStreaming.Subscription import Subscription
from Exercices.RecapStreaming.User import User

class StreamingService:

    def __init__(self,users:list, subscriptions:list):
        self.users = users
        self.subscriptions = subscriptions

    def new_user_subscription(self, new_user: User, subscription: Subscription):
        user = User(new_user.customer_number,new_user.firstname,new_user.lastname,new_user.email,subscription)
        self.users.append(user)

    def list_users_by_subscription(self, subscription_type: str):
        list_of_users = []
        for user in self.users:
            if user.subscription.name.lower() == subscription_type.lower():
                list_of_users.append(user)
        return list_of_users

    def billing_by_subscription(self, subscription_type: str) -> float:
        users_to_bill = self.list_users_by_subscription(subscription_type)
        users_billing_amount = 0
        for user in users_to_bill:
            users_billing_amount += user.subscription.price
        return users_billing_amount