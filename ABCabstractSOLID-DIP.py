from abc import ABC, abstractmethod

class MessageSender(ABC):
    @abstractmethod
    def send(self, message: str) -> None: ...
 
 
class EmailSender(MessageSender):
    def send(self, message: str) -> None:
        # send email
        print(f'Sending email with message: {message}')

class SMSSender(MessageSender):
    def send(self, message: str) -> None:
        # send sms
        print(f'Sending SMS with message: {message}')
 
class Task:
    def __init__(self, message_sender: MessageSender):
        self.message_sender = message_sender
 
    def process(self) -> None:
        # some processing things...
        self.message_sender.send('some nice message')

email_sender = EmailSender()
task1 = Task(email_sender)
task1.process()
sms_sender = SMSSender()
task2 = Task(sms_sender)
task2.process()