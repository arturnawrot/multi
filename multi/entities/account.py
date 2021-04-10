class Account:

    def __init__(self, email, password, cookies=None):
        self.email = email
        self.password = password
        self.cookies = cookies

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_cookies(self):
        return self.cookies

    def set_cookies(self, cookies):
        self.cookies = cookies
