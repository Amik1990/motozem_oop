from pages.base_page import BasePage
from playwright.sync_api import Locator
from utils.config import config
import re

class HomePage(BasePage):
    """
    Třída reprezentující domovskou stránku Motozem.
    Obsahuje metody pro interakci s prvky na této stránce.
    """

    def load(self) -> None:
        """
        Načte domovskou stránku a potvrdí cookies.
        """
        self.navigate(config.BASE_URL)
        self.accept_cookies()

    def is_banner_visible(self) -> None:
        """
        Ověří, že hlavní banner s logem MotoZem je viditelný.
        """
        banner = self.page.get_by_role("banner").get_by_role("link", name="MotoZem", exact=True)
        self.expect_visible(banner, name="Hlavní logo MotoZem")

    def poradime_vam_menu_is_visible(self) -> None:
        """
        Ověří, že tlačítko "Máte dotaz?" je viditelné.
        """
        poradime_button = self.page.get_by_label("Máte dotaz?")
        self.expect_visible(poradime_button, name="Tlačítko 'Máte dotaz?'")

    def poradime_vam_menu_content_is_present(self) -> None:
        """
        Otevře menu "Máte dotaz?" a ověří obsah (Napsat dotaz, telefonní číslo).
        """
        poradime_button = self.page.get_by_role("link", name="Máte dotaz?")
        self.click(poradime_button, name="Máte dotaz?")

        poradime_menu = [
            {"selector": self.page.get_by_role("link", name="Napsat dotaz"), "text": "Napsat dotaz"},
            {"selector": self.page.get_by_role("complementary").get_by_role("link", name="+420 555 333"),
             "text": "+420 555 333 957"},
        ]

        for item in poradime_menu:
            menu_item = item["selector"]
            item_name = item["text"]
            self.expect_visible(menu_item, name=item_name)
            self.to_have_text(menu_item, item["text"], name=item_name)

    def state_flags_are_visible(self) -> None:
        """
        Otevře menu s vlajkami a ověří viditelnost jednotlivých států.
        """
        state_flag = self.page.get_by_role("link", name="Motozem.cz", exact=True)
        self.hover(state_flag, name="Vlajka CZ")

        flag_items = [
            {"selector": self.page.get_by_role("link", name="Motozem.sk"), "name": "Motozem.sk"},
            {"selector": self.page.get_by_role("link", name="Motozem.hu"), "name": "Motozem.hu"},
            {"selector": self.page.get_by_role("link", name="Motozem.ro"), "name": "Motozem.ro"},
            {"selector": self.page.get_by_role("link", name="Motozem.sk"), "name": "Motozem.sk"},
            {"selector": self.page.get_by_role("link", name="Motozem.hr"), "name": "Motozem.hr"},
            {"selector": self.page.get_by_role("link", name="Motozem.pl"), "name": "Motozem.pl"},
            {"selector": self.page.get_by_role("link", name="Motozem.at"), "name": "Motozem.at"},
            {"selector": self.page.get_by_role("link", name="Motozem.de"), "name": "Motozem.de"},
            {"selector": self.page.get_by_role("link", name="Motozem.si"), "name": "Motozem.si"},
        ]

        for flag in flag_items:
            menu_item = flag["selector"]
            item_name = flag["name"]
            self.expect_visible(menu_item, name=item_name)

    def muj_ucet_is_visible(self) -> None:
        """
        Ověří, že tlačítko "Můj účet" je viditelné.
        """
        muj_ucet = self.page.get_by_role("link", name="Můj účet")
        self.expect_visible(muj_ucet, name="Tlačítko 'Můj účet'")

    def ucet_menu_is_visible_when_hoover_over_muj_ucet(self) -> None:
        """
        Najede na "Můj účet" a ověří, že se zobrazí menu pro přihlášení/registraci.
        """
        muj_ucet = self.page.get_by_role("link", name="Můj účet")
        muj_ucet_menu = self.page.get_by_text("Přihlásit Registrovat")
        self.hover(muj_ucet, name="Můj účet")
        self.expect_visible(muj_ucet_menu, name="Menu Můj účet")

    def prihlaseni_uzivatele_is_visible(self) -> None:
        """
        Otevře přihlašovací formulář z menu "Můj účet" a ověří jeho nadpis.
        """
        muj_ucet = self.page.get_by_role("link", name="Můj účet")
        prihlaseni_uzivatele_text = self.page.get_by_role("heading", name="Přihlášení uživatele")

        self.hover(muj_ucet, name="Můj účet")
        prihlasit = self.page.get_by_label("Přihlásit")
        self.click(prihlasit, name="Tlačítko Přihlásit")
        self.expect_visible(prihlaseni_uzivatele_text, name="Nadpis 'Přihlášení uživatele'")
