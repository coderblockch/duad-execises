class Email:
    def send_email(self, message):
        print(f"Sending email: {message}")

class PushMail:
    def send_push(self, message):
        print(f"Sending push notification: {message}")

class Messenger:
    def send_message(self, message):
        print(f"Sending instant message: {message}")


class Smartphone(Email, PushMail, Messenger):
    def __init__(self, brand):
        self.brand = brand


# Test
phone = Smartphone("Samsung")
print(f"Device: {phone.brand}")
phone.send_email("Meeting at 3pm")
phone.send_push("New notification")
phone.send_message("Hey, how are you?")