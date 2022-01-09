from multi.entities.ref import Ref
from multi.locators.list.list_locator import ListLocator
from multi.exceptions.page_not_retrieved import PageNotRetrieved
from tests.base_test import BaseTest

class ListLocatorTest(BaseTest):

    def setUp(self) -> None:
        self.list_locator = ListLocator()

    def test_gets_refs_to_unread_messages(self) -> None:
        html = self.get_fixture_content('buddylist/unread_messages.html')
        expected_refs = [
            Ref("Paul", "/messages/read/?tid=cid.c.100015784446089%3A100063745055206&ref_component=mbasic_home_header&ref_page=MChatBuddyListController#fua", 2),
            Ref("Stephen", "/messages/read/?tid=cid.c.100015784446089%3A100063488482176&ref_component=mbasic_home_header&ref_page=MChatBuddyListController#fua", 1)
        ]

        refs = self.list_locator.get_refs(html)

        self.assertEqual(refs, expected_refs)

    def test_gets_empty_list_if_no_updates(self):
        html = self.get_fixture_content('buddylist/no_updates.html')

        refs = self.list_locator.get_refs(html)

        self.assertEqual(refs, [])

    def test_throws_an_exception_for_invalid_html(self):
        html = '<h1>Access Denied</h1>'
        self.assertRaises(PageNotRetrieved, self.list_locator.get_refs, html)
