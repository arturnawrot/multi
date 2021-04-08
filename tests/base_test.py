import os
import unittest

fixtures_folder_location = "tests/fixtures/"

class BaseTest(unittest.TestCase):

    @staticmethod
    def get_fixture_content(location: str) -> str:
        path = os.path.join(fixtures_folder_location, location)
        with open(path, "r", encoding='utf-8') as f:
            return f.read()

