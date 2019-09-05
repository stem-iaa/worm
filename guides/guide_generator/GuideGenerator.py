from bs4 import BeautifulSoup as Soup


class GuideGenerator:
    def __init__(self, guide_template_path):
        self.guide_template_path = guide_template_path
        self.guide_source = open(self.guide_template_path, "r").read()
        self.guide_soup = Soup(self.guide_source)

        print(self.guide_soup)

    def add_account(self, username, password):
        pass

    def generate_guides(self, output_dir):
        pass


if __name__ == '__main__':
    generator = GuideGenerator("../")
