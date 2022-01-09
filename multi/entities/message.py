class Message:

    def __init__(self, sender: str, content: str, received_date: str):
        self.sender = sender
        self.content = content
        self.received_date = received_date

    def __eq__(self, other):
        return self.sender == other.sender and \
               self.content == other.content and \
               self.received_date == other.received_date

    def get_sender(self) -> str:
        return self.sender

    def get_content(self) -> str:
        return self.content

    def get_received_date(self) -> str:
        return self.received_date
