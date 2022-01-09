class Lisitng:

    def __init__(self, url: str, is_working: int):
        self.url = url

    def __eq__(self, other):
        return self.url == other.url

    def get_url(self) -> str:
        return self.url

    def is_working(self) -> bool:
        return self.is_working