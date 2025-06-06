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

    def state_flag_is_visible(self):
        state_flag = self.page.get_by_role("link", name="Motozem.cz", exact=True)
        expect(state_flag).to_be_visible()

    def state_flags_are_visible_when_hover_over(self):
        state_flag = self.page.get_by_role("link", name="Motozem.cz", exact=True)
        state_flag.hover()

        flag_items = [
            {"selector": self.page.get_by_role("link", name="Motozem.sk"), "aria_label": "Motozem.sk"},
            {"selector": self.page.get_by_role("link", name="Motozem.hu"), "aria_label": "Motozem.hu"},
            {"selector": self.page.get_by_role("link", name="Motozem.pl"), "aria_label": "Motozem.pl"},
            {"selector": self.page.get_by_role("link", name="Motozem.at"), "aria_label": "Motozem.at"},
            {"selector": self.page.get_by_role("link", name="Motozem.de"), "aria_label": "Motozem.de"},
            {"selector": self.page.get_by_role("link", name="Motozem.ro"), "aria_label": "Motozem.ro"},
            {"selector": self.page.get_by_role("link", name="Motozem.hr"), "aria_label": "Motozem.hr"},
            {"selector": self.page.get_by_role("link", name="Motozem.si"), "aria_label": "Motozem.si"},
        ]

        for flag in flag_items:
            menu_item = flag["selector"]
            expect(menu_item).to_be_visible()
            expect(menu_item).to_have_attribute("aria-label", flag["aria_label"])


    def muj_ucet_is_visible(self):
        muj_ucet = self.page.get_by_role("link", name="Můj účet")
        expect(muj_ucet).to_be_visible()

    def ucet_menu_is_visible_when_hoover_over_muj_ucet(self):
        muj_ucet = self.page.get_by_role("link", name="Můj účet")
        muj_ucet_menu = self.page.get_by_text("Přihlásit Registrovat")
        muj_ucet.hover()
        expect(muj_ucet_menu).to_be_visible()

    def prihlaseni_uzivatele_is_visible(self):
        muj_ucet = self.page.get_by_role("link", name="Můj účet")
        prihlaseni_uzivatele_text = self.page.get_by_role("heading", name="Přihlášení uživatele")

        muj_ucet.hover()
        prihlasit = self.page.get_by_label("Přihlásit")
        prihlasit.click()
        expect(prihlaseni_uzivatele_text).to_have_text("Přihlášení uživatele")