from pages.base_page import BasePage
from playwright.sync_api import expect

class HomePage(BasePage):

    def load(self):
        self.page.goto("https://www.motozem.cz/")
        button = self.page.get_by_role("link", name="OK", exact=True)
        self.click(button)

    def is_banner_visible(self):
        banner = self.page.get_by_role("banner").get_by_role("link", name="MotoZem", exact=True)
        expect(banner).to_be_visible()

    def poradime_vam_menu_is_visible(self):
        poradime_button = self.page.get_by_label("Máte dotaz?")
        expect(poradime_button).to_be_visible()

    def poradime_vam_menu_content_is_present(self):
        poradime_button = self.page.get_by_role("link", name="Máte dotaz?")
        poradime_button.click()

        poradime_menu = [
            {"selector": self.page.get_by_role("link", name="Napsat dotaz"), "text": "Napsat dotaz"},
            {"selector": self.page.get_by_role("complementary").get_by_role("link", name="+420 555 333"),
             "text": "+420 555 333 957"},
        ]

        for item in poradime_menu:
            menu_item = item["selector"]
            expect(menu_item).to_be_visible()
            expect(menu_item).to_have_text(item["text"])