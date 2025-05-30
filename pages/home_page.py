from pages.base_page import BasePage
from playwright.sync_api import expect

class HomePage(BasePage):

    def load(self):
        self.page.goto("https://www.motozem.cz/")

    def is_banner_visible(self):
        banner = self.page.get_by_role("banner").get_by_role("link", name="MotoZem", exact=True)
        expect(banner).to_be_visible()