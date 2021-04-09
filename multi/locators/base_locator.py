from lxml import etree

class BaseLocator:

    @staticmethod
    def get_tree_from_html(html: str):
        return etree.HTML(html.encode())

    @staticmethod
    def does_element_exist(html) -> bool:
        if html == None:
            return False

        if len(html) == 0:
            return False

        return True
