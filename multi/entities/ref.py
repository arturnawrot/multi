from multi.scrapers.urls import ROOT_URL

class Ref:

    def __init__(self, name: str, link: str, number_of_new_messages: int):
        self.name = name
        self.link = link
        self.number_of_new_messages = number_of_new_messages

    def __eq__(self, other):
        return self.name == other.name and \
               self.link == other.link and \
               self.number_of_new_messages == other.number_of_new_messages

    def get_name(self) -> str:
        return self.name

    def get_link(self) -> str:
        return self.link

    def get_number_of_new_messages(self) -> int:
        return self.number_of_new_messages

    def get_full_url_to_chat(self):
        return ROOT_URL + self.link