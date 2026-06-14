from abc import ABC ,abstractmethod
class NotificationChannel(ABC):
    @abstractmethod
    def send_notification(self,message):
        pass
    

class EmailChannel(NotificationChannel):
    def send_notification(self,message):
        print(f"Sending EMAIL: {message}")

class SMSChannel(NotificationChannel):
    def send_notification(self,message):
        print(f"Sending SMS: {message}")
class PushChannel(NotificationChannel):
    def send_notification(self,message):
        print(f"Sending PUSH: {message}")
class SlackChannel(NotificationChannel):
    def send_notification(self,message):
        print(f"Sending SLACK: {message}")


class NotificationService:
    def __init__(self,notification_type: NotificationChannel):
        self.notification_type=notification_type
        
    def send_notification(self, message: str) -> None:
        self.notification_type.send_notification(message)
       
# Usage
emailservice = NotificationService(EmailChannel())
smsservice = NotificationService(SMSChannel())
pushservice = NotificationService(PushChannel())
slackservice = NotificationService(SlackChannel())

emailservice.send_notification("Your order has shipped!")
smsservice.send_notification("Your order has shipped!")
pushservice.send_notification("Your order has shipped!")
slackservice.send_notification("Your order has shipped!")

# TODO: Define a NotificationChannel interface (ABC) with a send(message) method.
# TODO: Create EmailChannel, SMSChannel, PushChannel, and SlackChannel.
# TODO: Refactor NotificationService to accept a NotificationChannel.