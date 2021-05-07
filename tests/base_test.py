import os
import unittest
from env import FIXTURES_DIR

class BaseTest(unittest.TestCase):

    @staticmethod
    def get_full_path(location: str):
        return os.path.join(FIXTURES_DIR, location)

    def get_fixture_content(self, location: str) -> str:
        path = self.get_full_path(location)
        with open(path, "r", encoding='utf-8') as f:
            return f.read()