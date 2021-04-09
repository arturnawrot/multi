from multi.entities.ref import Ref
from multi.locators.list.paths import REFS, NAV_CHAT_LINK
from multi.exceptions.page_not_retrieved import PageNotRetrieved
from multi.locators.base_locator import BaseLocator

class ListLocator(BaseLocator):

    def get_refs(self, html: str) -> list:
        tree = self.get_tree_from_html(html)

        chat_link = tree.xpath(NAV_CHAT_LINK)
        if not self.does_element_exist(chat_link):
            raise PageNotRetrieved

        html_refs = tree.xpath(REFS)

        refs = []

        for html_ref in html_refs:
            name = html_ref.text.split('(')[0]
            link = html_ref.get('href')
            number_of_messages = int(html_ref.get('aria-label')[0])

            refs.append(Ref(name, link, number_of_messages))

        return refs

