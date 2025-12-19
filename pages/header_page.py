from pages.base_page import BasePage
from playwright.sync_api import expect

class HeaderPage(BasePage):

    def load(self):
        self.navigate("https://www.motozem.cz/")
        self.accept_cookies()

    def informace_menu_is_visible_when_hover_over(self):
        informace_button = self.page.get_by_role("link", name="Informace")
        informace_menu = self.page.get_by_text("O nás Obchodní podmínky Ochrana osobních údajů Velkoobchod Prodejny Články Vnit")
        informace_button.hover()
        expect(informace_menu).to_be_visible()

    def informace_menu_content(self):
        informace_button = self.page.get_by_role("link", name="Informace")
        informace_button.hover()

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
            expect(menu_item).to_be_visible()
            expect(menu_item).to_have_text(item["text"])

    def prodejny_menu_is_visible_when_hover_over(self):
        prodejny_button = self.page.get_by_role("banner").get_by_role("link", name="Prodejny")
        prodejny_menu = self.page.locator("li").filter(has_text="Prodejny Dobrá Brno Čestlice").get_by_role("list")
        prodejny_button.hover()
        expect(prodejny_menu).to_be_visible()

    def prodejny_menu_content(self):
        prodejny_button = self.page.get_by_role("banner").get_by_role("link", name="Prodejny")
        prodejny_button.hover()

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
            expect(menu_item).to_be_visible()
            expect(menu_item).to_have_text(item["text"])