from lxml import etree
from multi.entities.ref import Ref
from multi.locators.list.paths import REFS, NAV_CHAT_LINK
from multi.exceptions.page_not_retrieved import PageNotRetrieved

class ListLocator:

    def get_refs(self, html_source: str) -> list:
        tree = etree.HTML(html_source.encode())

        if len(tree.xpath(NAV_CHAT_LINK)) == 0:
            raise PageNotRetrieved

        html_refs = tree.xpath(REFS)

        refs = []

        for html_ref in html_refs:
            name = html_ref.text.split('(')[0]
            link = html_ref.get('href')
            number_of_messages = int(html_ref.get('aria-label')[0])

            refs.append(Ref(name, link, number_of_messages))

        return refs

