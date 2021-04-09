from multi.entities.message import Message
from multi.locators.base_locator import BaseLocator
from multi.locators.chat.paths import MESSAGE_BLOCKS, SENDER, MESSAGES, MESSAGE_CONTENT, OLDER_MESSAGES_SPAN, SEND_INPUT
from multi.exceptions.page_not_retrieved import PageNotRetrieved
from multi.utils.date import get_local_time

class ChatLocator(BaseLocator):

    def get_messages(self, html: str) -> list:
        tree = self.get_tree_from_html(html)

        send_button = tree.xpath(SEND_INPUT)
        if not self.does_element_exist(send_button):
            raise PageNotRetrieved

        blocks = tree.xpath(MESSAGE_BLOCKS)

        messages = []

        for block in blocks:
            messages.extend(self.get_messages_from_block(block))

        return messages

    def get_messages_from_block(self, block) -> list:
        sender = block.xpath(SENDER)
        html_messages = block.xpath(MESSAGES)

        messages = []

        for html_message in html_messages:
                messages_list = html_message.xpath(MESSAGE_CONTENT)

                if not self.does_element_exist(messages_list):
                    continue

                for message_str in messages_list:
                    messages.append(Message(sender, message_str, get_local_time()))

        return messages

    def does_have_older_messages(self, html: str) -> bool:
        tree = self.get_tree_from_html(html)
        element = tree.xpath(OLDER_MESSAGES_SPAN)

        return self.does_element_exist(element)
