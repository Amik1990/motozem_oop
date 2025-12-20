from pages.base_page import BasePage
from playwright.sync_api import expect

class HeaderPage(BasePage):

    def load(self):  # pouzije se pak v fixture_utils.py v setup_page casti try  instance.load
        self.navigate("https://www.motozem.cz/")
        self.accept_cookies()

    def informace_menu_is_visible_when_hover_over(self):
        informace_button = self.page.get_by_role("link", name="Informace")
        informace_menu = self.page.get_by_text("O nás Obchodní podmínky Ochrana osobních údajů Velkoobchod Prodejny Články Vnit")
        self.hover(informace_button, name="Informace")
        self.expect_visible(informace_menu, name="O nás Obchodní podmínky Ochrana osobních údajů Velkoobchod Prodejny Články Vnit")

    def informace_menu_content(self):
        informace_button = self.page.get_by_role("link", name="Informace")
        self.hover(informace_button, name="Informace")

        informace_items = [
            {"selector": self.page.get_by_title("O nás"), "text": "O nás"},
            {"selector": self.page.get_by_title("Obchodní podmínky"), "text": "Obchodní podmínky"},
            {"selector": self.page.get_by_title("Ochrana osobních údajů"), "text": "Ochrana osobních údajů"},
            {"selector": self.page.get_by_title("Velkoobchod"), "text": "Velkoobchod"},
            {"selector": self.page.get_by_title("Prodejny"), "text": "Prodejny"},
            {"selector": self.page.get_by_title("Vnitřní oznamovací systém"), "text": "Vnitřní oznamovací systém"},
            {"selector": self.page.get_by_title("Výměna, vrácení, reklamace"), "text": "Výměna, vrácení, reklamace"},
            {"selector": self.page.get_by_title("Kariéra"), "text": "Kariéra"},
        ]

        for item in informace_items:
            menu_item = item["selector"]
            item_text = item["text"]
            self.expect_visible(menu_item, name=item_text)
            self.to_have_text(menu_item, item_text, name=item_text)

    def prodejny_menu_is_visible_when_hover_over(self):
        prodejny_button = self.page.get_by_role("banner").get_by_role("link", name="Prodejny")
        prodejny_menu = self.page.locator("li").filter(has_text="Prodejny Dobrá Brno Čestlice").get_by_role("list")
        self.hover(prodejny_button, name="Prodejny")
        self.expect_visible(prodejny_menu, name="Prodejny Dobrá Brno Čestlice")

    def prodejny_menu_content(self):
        prodejny_button = self.page.get_by_role("banner").get_by_role("link", name="Prodejny")
        self.hover(prodejny_button, name="Prodejny")

        prodejny_items = [
            {"selector": self.page.get_by_title("Dobrá"), "text": "Dobrá"},
            {"selector": self.page.get_by_title("Brno"), "text": "Brno"},
            {"selector": self.page.get_by_title("Čestlice"), "text": "Čestlice"},
            {"selector": self.page.get_by_title("Senec"), "text": "Senec"},
            {"selector": self.page.get_by_title("Plzeň"), "text": "Plzeň"},
            {"selector": self.page.get_by_title("Košice"), "text": "Košice"},
        ]

        for item in prodejny_items:
            menu_item = item["selector"]
            item_text = item['text']
            self.expect_visible(menu_item, name=item_text)
            self.to_have_text(menu_item, item_text, name=item_text)

