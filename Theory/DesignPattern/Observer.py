
class BeAlert:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def send_alert(self, msg):
        for subscriber in self.subscribers:
            subscriber.display_message(msg)

class Subscriber:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def display_message(self,msg):
        print(f"{self.fullname()} has received a message: {msg}")

beAlert = BeAlert()
beAlert.subscribe(Subscriber("John", "Doe"))
beAlert.subscribe(Subscriber("Jane", "Doe"))
beAlert.subscribe(Subscriber("Scarlett", "Johansson"))

beAlert.send_alert("Fire nearby: close your doors and windows, and keep inside!")
