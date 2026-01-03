from pages.base_page import BasePage
from playwright.sync_api import expect
import re
from utils.config import config

class ShoppingCartPage(BasePage):
    """
    Třída reprezentující nákupní košík.
    """

    def load(self) -> None:
        """
        Načte domovskou stránku (košík je prázdný, začínáme nákupem) a potvrdí cookies.
        """
        self.navigate(config.BASE_URL)
        self.accept_cookies()

    def add_to_shopping_cart(self) -> None:
        """
        Vyhledá produkt, přidá ho do košíku a ověří, že se počet položek v košíku změnil.
        """
        revit_tornado = self.page.get_by_text(
            re.compile(r"Bunda na motorku Revit Tornado 4 H2O černo-antracitová.*Skladem")    # Bez re.compile by Playwright hledal ten text doslovně (včetně těch teček a hvězdičky), což by na stránce nenašel.
        )
        lupa = self.page.get_by_role("button", name="Hledat")
        medium_size = self.page.locator("label").filter(has_text="M").nth(1).first
        koupit_button = self.page.get_by_role("button", name="Koupit")
        pocet_v_kosiku_dva = self.page.locator("a").filter(has_text=re.compile(r"^2$"))

        self.page.get_by_role("banner").get_by_role("textbox").fill("revit tornado 4")
        self.click_and_wait_for_response(lupa,r"(?i)search", name="Hledat")

      #  self.click(lupa, name="Hledat")
        self.expect_visible(revit_tornado, name="Bunda na motorku Revit Tornado 4 H2O černo-antracitová.*Skladem", timeout=10000)
        self.click(revit_tornado, name="Revit Tornado 4")
        self.click(medium_size, name="Medium size")
        
        # Klikneme a čekáme na odpověď serveru (basket/košík)
        self.click_and_wait_for_response(koupit_button, r"basket|kosik", name="Koupit")
        
        # Ověření, že košík ukazuje 2 položky
        self.expect_visible(pocet_v_kosiku_dva, name="Počet v košíku: 2", timeout=10000)
        self.to_have_text(pocet_v_kosiku_dva, "2", name="Počet v košíku: 2")

    def change_amount_in_shopping_cart(self) -> None:
        """
        Přidá produkt do košíku, přejde do košíku a změní množství položek (+ a -).
        """
        self.add_to_shopping_cart()
        
        do_kosiku_button = self.page.get_by_role("link", name="Do košíku")
        self.click(do_kosiku_button, name="Do košíku")

        plus_button = self.page.locator("button[name=\"add\"]")
        minus_button = self.page.locator("button[name=\"sub\"]")
        pocet_bund = self.page.locator("input[name=\"iBasketProductCount\"]")

        # 1. Zvýšení množství (+)
        self.click_and_wait_for_response(plus_button, r"(?i)basket|kosik", name="Tlačítko Plus (+)")   # r"(?i)basket|kosik"  bude brát v potaz velká i malá písmena
        self.to_have_value(pocet_bund, "2", name="Input počet kusů (po plus)")

        # 2. Snížení množství (-)
        self.click_and_wait_for_response(minus_button, r"(?i)basket|kosik", name="Tlačítko Mínus (-)")
        self.to_have_value(pocet_bund, "1", name="Input počet kusů (po mínus)")
