from pages.base_page import BasePage
from playwright.sync_api import expect
import re

class ShoppingCartPage(BasePage):

    def load(self):
        self.navigate("https://www.motozem.cz/")
        self.accept_cookies()

    def add_to_shopping_cart(self):
        self.page.get_by_role("banner").get_by_role("textbox").fill("revit tornado 4")
        revit_tornado = self.page.get_by_text(
            re.compile(r"Bunda na motorku Revit Tornado 4 H2O černo-antracitová.*Skladem")
        )
        lupa = self.page.get_by_role("button", name="Hledat")
        medium_size = self.page.locator("label").filter(has_text="M").nth(1).first
        koupit_button = self.page.get_by_role("button", name="Koupit")
        pocet_v_kosiku_dva = self.page.locator("a").filter(has_text=re.compile(r"^2$"))

        lupa.click()
        expect(revit_tornado).to_be_visible(timeout=10000)
        revit_tornado.click()
        medium_size.click()
        koupit_button.click()
        expect(pocet_v_kosiku_dva).to_have_text("2")

    def change_amount_in_shopping_cart(self):
        self.add_to_shopping_cart()
        do_kosiku_button = self.page.get_by_role("link", name="Do košíku")
        pocet_bund = self.page.locator("input[name=\"iBasketProductCount\"]")
        pridat = self.page.locator("button[name=\"add\"]")
        odebrat = self.page.locator("button[name=\"sub\"]")

        do_kosiku_button.click()
        pridat.click()
        expect(pocet_bund).to_have_value("2")
        pridat.click()
        expect(pocet_bund).to_have_value("3")
        pridat.click()
        expect(pocet_bund).to_have_value("4")
        odebrat.click()
        expect(pocet_bund).to_have_value("3")
