from multi.locators.base_locator import BaseLocator
from multi.exceptions.page_not_retrieved import PageNotRetrieved
from multi.locators.navbar.paths import NAVBAR_MESSAGES_A, NUMBER_OF_UNREAD_MESSAGES

class NavbarLocator(BaseLocator):

    def get_number_of_unread_messages(self, html: str) -> int:
        tree = self.get_tree_from_html(html)

        navbar_messages_a = tree.xpath(NAVBAR_MESSAGES_A)
        if not self.does_element_exist(navbar_messages_a):
            raise PageNotRetrieved
        
        number_of_unread_messages = tree.xpath(NUMBER_OF_UNREAD_MESSAGES)

        if not self.does_element_exist(number_of_unread_messages):
            return 0

        number_of_unread_messages = number_of_unread_messages[0]

        # Ex. "(2)". We still need to get rid of parentheses
        number_of_unread_messages = number_of_unread_messages.replace('(','').replace(')','')

        return number_of_unread_messages

        