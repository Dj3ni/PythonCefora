from Exercices.RecapStreaming.StreamingService import StreamingService
from Exercices.RecapStreaming.Subscription import BasicSubscription, PremiumSubscription, StandardSubscription
from Exercices.RecapStreaming.User import User

basic = BasicSubscription()
standard = StandardSubscription()
premium = PremiumSubscription()

users = [
    User("123456", "John", "Doe", "john.doe@mail.com", basic),
    User("234567", "Jane", "Doe", "jane.doe@mail.com", basic),
    User("345678", "Brad", "Pit", "brad.pit@mail.com", standard),
    User("456789", "Scarlett", "Johansson", "scarlett.j@mail.com", premium),
]

subscriptions = [basic, standard, premium]

netflix = StreamingService(users, subscriptions)

for user in netflix.users:
    print(user.fullname())

for user in netflix.list_users_by_subscription(basic.name):
    print(user.fullname())
    print(user.subscription.name)

print(f"Total billing for {basic.name} abo: {netflix.billing_by_subscription(basic.name)} €")


"""
u1 = users[0]
u1.change_subscription(StandardSubscription())
u1.change_subscription(PremiumSubscription())

for user in users:
    print(user.fullname())

    for i in user.historical_subscriptions_billing:
        print(i)
"""