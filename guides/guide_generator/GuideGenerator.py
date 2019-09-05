from bs4 import BeautifulSoup as Soup
from Account import Account


class GuideGenerator:
    def __init__(self, guide_template_path):
        self.guide_template_path = guide_template_path
        self.guide_source = open(self.guide_template_path, "r").read()
        self.guide_soup = Soup(self.guide_source)

        self.accounts = []

    def add_account(self, username, password):
        account = Account(username=username, password=password)
        self.accounts.append(account)

    def generate_guides(self, output_dir):
        username_element = self.guide_soup.find("mark", {"id": "username"})
        password_element = self.guide_soup.find("mark", {"id": "password"})

        for account in self.accounts:
            username_element.string = account.username
            password_element.string = account.password
            open(output_dir + "/" + account.username + ".md", "w").write(str(self.guide_soup))


if __name__ == '__main__':
    generator = GuideGenerator("../getting_started/StudentGettingStarted.md")
    generator.add_account("test_username", "test_password")
    generator.add_account("test_username2", "test_password2")
    generator.generate_guides(".")
