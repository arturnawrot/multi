class MarketplaceProfile:

    def __init__(self, url: str):
        self.url = url

    def __eq__(self, other):
        return self.url == other.url

    def get_url(self) -> str:
        return self.url