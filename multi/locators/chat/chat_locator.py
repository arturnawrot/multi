from multi.entities.conversation_chunk import ConversationChunk
from multi.entities.message import Message
from multi.locators.base_locator import BaseLocator
from multi.locators.chat.paths import *
from multi.exceptions.page_not_retrieved import PageNotRetrieved
from multi.utils.date import get_local_time

class ChatLocator(BaseLocator):

    def get_conversation_chunk(self, html: str) -> list:
        tree = self.get_tree_from_html(html)

        send_button = tree.xpath(SEND_INPUT)
        if not self.does_element_exist(send_button):
            raise PageNotRetrieved

        older_messages_url = None
        if self.has_older_messages(html):
            older_messages_url = tree.xpath(OLDER_MESSAGES_URL)

        rows = tree.xpath(MESSAGE_BLOCKS)

        messages = []

        for row in rows:
            messages.extend(self.get_messages(row))

        return ConversationChunk(messages, get_local_time(), older_messages_url)

    def get_messages(self, row) -> list:
        sender = row.xpath(SENDER)
        html_messages = row.xpath(MESSAGES)

        messages = []

        for html_message in html_messages:
                messages_list = html_message.xpath(MESSAGE_CONTENT)

                if not self.does_element_exist(messages_list):
                    continue

                for message_str in messages_list:
                    messages.append(Message(sender, message_str, get_local_time()))

        return messages

    def has_older_messages(self, html: str) -> bool:
        tree = self.get_tree_from_html(html)
        element = tree.xpath(OLDER_MESSAGES_SPAN)

        return self.does_element_exist(element)
