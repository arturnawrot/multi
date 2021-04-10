from multi.locators.chat.chat_locator import ChatLocator
from multi.exceptions.page_not_retrieved import PageNotRetrieved
from multi.entities.conversation_chunk import ConversationChunk
from multi.entities.message import Message
from multi.utils.date import get_local_time
from tests.base_test import BaseTest

class ChatLocatorTest(BaseTest):

    def setUp(self) -> None:
        self.chat_locator = ChatLocator()

    def test_reads_messages(self) -> None:
        html = self.get_fixture_content('chat/older_messages.html')

        messages = self.chat_locator.get_conversation_chunk(html)
        local_time = get_local_time()

        expected_messages = ConversationChunk([
                Message('Paul Hirthe', '???', local_time),
                Message('Arthur Nawrot', 'Yes?', local_time),
                Message('Paul Hirthe', 'How are you?', local_time),
                Message('Paul Hirthe', 'I missed you so much', local_time),
                Message('Paul Hirthe', 'Please reply', local_time),
            ],
            local_time,
            "/messages/read/?tid=cid.c.100015784446089%3A100063745055206&last_message_timestamp=1617904960579&pagination_direction=1&show_delete_message_button&refid=12"
        )

        self.assertEqual(messages, expected_messages)

    def test_older_messages(self) -> None:
        html = self.get_fixture_content('chat/older_messages.html')
        cond = self.chat_locator.has_older_messages(html)

        self.assertTrue(cond)

        html = self.get_fixture_content('chat/no_older_messages.html')
        cond = self.chat_locator.has_older_messages(html)

        self.assertFalse(cond)

    def test_throws_an_exception_for_invalid_html(self):
        html = '<h1>Access Denied</h1>'
        self.assertRaises(PageNotRetrieved, self.chat_locator.get_conversation_chunk, html)
