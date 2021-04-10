class ConversationChunk:

    def __init__(self, messages, received_date: str, url_to_previous_chunk: str):
        self.messages = messages
        self.received_date = received_date
        self.url_to_previous_chunk = url_to_previous_chunk

    def __eq__(self, other):
        return self.messages == other.messages and \
               self.received_date == other.received_date and \
               self.url_to_previous_chunk == other.url_to_previous_chunk

    def get_messages(self):
        return self.messages

    def get_received_date(self):
        return self.received_date

    def get_url_to_previous_chunk(self):
        return self.url_to_previous_chunk
