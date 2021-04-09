from multi.locators.chat.chat_locator import ChatLocator
from multi.exceptions.page_not_retrieved import PageNotRetrieved
from multi.entities.message import Message
from multi.utils.date import get_local_time
from tests.base_test import BaseTest

class ChatLocatorTest(BaseTest):

    def setUp(self) -> None:
        self.chat_locator = ChatLocator()

    def test_reads_messages(self) -> None:
        html = self.get_fixture_content('chat/older_messages.html')

        messages = self.chat_locator.get_messages(html)
        local_time = get_local_time()

        expected_messages = [
            Message('Paul Hirthe', '???', local_time),
            Message('Arthur Nawrot', 'Yes?', local_time),
            Message('Paul Hirthe', 'How are you?', local_time),
            Message('Paul Hirthe', 'I missed you so much', local_time),
            Message('Paul Hirthe', 'Please reply', local_time),
        ]

        self.assertEqual(messages, expected_messages)

    def test_older_messages(self) -> None:
        html = self.get_fixture_content('chat/older_messages.html')
        cond = self.chat_locator.does_have_older_messages(html)

        self.assertTrue(cond)

        html = self.get_fixture_content('chat/no_older_messages.html')
        cond = self.chat_locator.does_have_older_messages(html)

        self.assertFalse(cond)

    def test_throws_an_exception_for_invalid_html(self):
        html = '<h1>Access Denied</h1>'
        self.assertRaises(PageNotRetrieved, self.chat_locator.get_messages, html)
