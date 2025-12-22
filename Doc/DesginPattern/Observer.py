class BeAlert:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def send_message(self, msg):
        for subscriber in self.subscribers:
            subscriber.display_message(msg)


class Subscriber:
    def __init__(self, name):
        self.name = name

    def display_message(self, msg):
        print(f"{self.name} a reçu '{msg}' par sms")

beAlert = BeAlert()

beAlert.subscribe(Subscriber("Jean"))
beAlert.subscribe(Subscriber("Léonidas"))

beAlert.send_message("Bienvenue dans le cours")