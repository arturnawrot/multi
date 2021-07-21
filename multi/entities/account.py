class Account:

    def __init__(self, email, password, cookies=None, chat_link=None, name=None):
        self.email = email
        self.password = password
        self.cookies = cookies
        self.chat_link = chat_link
        self.name = name

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_cookies(self):
        return self.cookies

    def set_cookies(self, cookies):
        self.cookies = cookies

    def get_chat_link(self):
        return self.chat_link

    def get_name(self):
        return self.name
