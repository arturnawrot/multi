from multi.scrapers.urls import ROOT_URL
import json

class Ref:

    def __init__(self, name: str, link: str, number_of_new_messages: int):
        self.name = name
        self.link = link
        self.number_of_new_messages = number_of_new_messages

    def __eq__(self, other):
        return self.name == other.name and \
               self.link == other.link and \
               self.number_of_new_messages == other.number_of_new_messages

    def __repr__(self) -> str:
        return f"Ref(Name: {self.get_name()}, Link: {self.get_link()}, Num. of new messages: {self.get_number_of_new_messages()})"

    def get_name(self) -> str:
        return self.name

    def get_link(self) -> str:
        return self.link

    def get_number_of_new_messages(self) -> int:
        return self.number_of_new_messages

    def get_full_url_to_chat(self):
        return ROOT_URL + self.link

    def serialize(self):
        return {
            'name': self.get_name(), 
            'link': self.get_link(),
            'number_of_new_messages': self.get_number_of_new_messages(),
        }